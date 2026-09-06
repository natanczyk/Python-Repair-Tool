from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

from LLMs.llm import QwenLLM
from Localization.fauxpy_runner import FauxPyRunner
from Localization.program import Program


# -----------------------------------------------------------------------------
# Prompt builders
#
# Three functions, each with two variants controlled by a flag:
#   1. build_feedback_prompt        - for the Feedback_Agent
#   2. build_repair_prompt          - first repair attempt
#   3. build_followup_repair_prompt - every attempt after the first
# -----------------------------------------------------------------------------

def _extract_code(response: str) -> str:
    match = re.search(r"```(?:python)?\n(.*?)```", response, re.DOTALL)
    if match:
        return match.group(1).strip()
    return response.strip()


_FEEDBACK_HEADER = (
    "You are an educational Python debugging assistant helping a novice student.\n"
    "Do NOT reveal the corrected code or solution.\n"
    "Do not use code blocks or markdown."
)

_FEEDBACK_BASE = (
    "Provide:\n"
    "1. A short explanation of what is likely wrong\n"
    "2. A hint that guides the student toward the fix"
)


def build_feedback_prompt_empty(description: str) -> str:
    """Edge case: student submitted an empty file."""
    return f"""{_FEEDBACK_HEADER}

Assignment:
{description}

The student submitted an empty file - no code was provided.
Let the student know their submission was empty and encourage them to attempt the assignment.""".strip()


def build_feedback_prompt_syntax_error(
    description: str,
    student_code: str,
    syntax_error: str,
) -> str:
    """Edge case: student code has a syntax error and cannot be executed."""
    return f"""{_FEEDBACK_HEADER}

Assignment:
{description}

Student code:
{student_code}

The code cannot run because of a syntax error:
{syntax_error}

Explain what a syntax error is, point the student to the specific line, and give a hint on how to fix it.""".strip()


def build_feedback_prompt_basic(description: str, student_code: str) -> str:
    """Type 1: description + student code only."""
    return f"""{_FEEDBACK_HEADER}

Assignment:
{description}

Student code:
{student_code}

{_FEEDBACK_BASE}""".strip()


def build_feedback_prompt_with_tests(
    description: str,
    student_code: str,
    failing_tests: str | None,
) -> str:
    """Type 2: + failing tests. Falls back to basic if failing_tests is unavailable."""
    if not failing_tests:
        return build_feedback_prompt_basic(description, student_code)
    return f"""{_FEEDBACK_HEADER}

Assignment:
{description}

Student code:
{student_code}

Failing tests (call -> expected result):
{failing_tests}

{_FEEDBACK_BASE}""".strip()


def build_feedback_prompt_with_localization(
    description: str,
    student_code: str,
    suspicious_lines: str | None,
) -> str:
    """Type 3: + FauxPy suspicious lines. Falls back to basic if localization is unavailable."""
    if not suspicious_lines:
        return build_feedback_prompt_basic(description, student_code)
    return f"""{_FEEDBACK_HEADER}

Assignment:
{description}

Student code:
{student_code}

Most suspicious lines (focus your hint here):
{suspicious_lines}

{_FEEDBACK_BASE}""".strip()


def build_llm_localization_prompt(
    description: str,
    student_code: str,
    failing_tests: str | None,
) -> str:
    """Asks the LLM to identify the most suspicious lines before giving feedback."""
    failing_section = f"\nFailing tests:\n{failing_tests}" if failing_tests else ""
    return f"""Given the following buggy Python code and its failing tests, identify the most suspicious lines that likely contain the bug.
List only line numbers and a brief reason for each. Do not fix the code, do not use code blocks.

Assignment:
{description}
{failing_section}

Student code:
{student_code}

Which lines are most suspicious and why?""".strip()


def build_feedback_prompt_with_repair(
    description: str,
    student_code: str,
    repaired_code: str | None,
) -> str:
    """Type 4: + repaired code as internal reference. Falls back to basic if repair is unavailable."""
    if not repaired_code:
        return build_feedback_prompt_basic(description, student_code)
    return f"""{_FEEDBACK_HEADER}
An internal repaired version is provided for your reference only - do NOT quote or reveal it.

Assignment:
{description}

Student code:
{student_code}

Internal repaired version (do not reveal to the student):
{repaired_code}

Provide:
1. What concept the student likely misunderstood
2. Which specific part of their code to inspect
3. A hint that guides them toward the fix without giving it away""".strip()


def build_repair_prompt(
    description: str,
    student_code: str,
    failing_tests: str | None,
    suspicious_lines: str | None = None,
) -> str:
    """First repair attempt - always uses FauxPy suspicious lines when available."""
    failing_section = (
        f"\n### Failing Tests (call -> expected result) ###\n{failing_tests}"
        if failing_tests else ""
    )
    loc_section = (
        f"\n### These are the most likely suspicious Lines, try to focus on these ###\n{suspicious_lines}"
        if suspicious_lines else ""
    )

    return f"""
Fix all bugs in the Python program below.
Modify the code as little as possible.
Return ONLY the corrected Python code, no explanation.
Do NOT rename functions or change signatures. Focus only on fixing the bug, not on refactoring or improving the code style.

### Assignment ###
{description}
{failing_section}
{loc_section}

### Buggy Code ###
```python
{student_code}
```
""".strip()


def build_followup_repair_prompt(
    description: str,
    previous_code: str,
    failing_tests: str | None,
    suspicious_lines: str | None = None,
) -> str:
    """Every repair attempt after the first - always uses FauxPy suspicious lines when available."""
    failing_section = (
        f"\n### Failing Tests (call -> expected result) ###\n{failing_tests}"
        if failing_tests else ""
    )
    loc_section = (
        f"\n### These are the most likely suspicious Lines, try to focus on these ###\n{suspicious_lines}"
        if suspicious_lines else ""
    )

    return f"""
Your previous repair was incorrect - the following tests still fail.
Try again. Modify the code as little as possible.
Return ONLY the corrected Python code, no explanation.
Do NOT rename functions or change signatures. Focus only on fixing the bug, not on refactoring or improving the code style.
### Assignment ###
{description}
{failing_section}
{loc_section}

### Previous Incorrect Repair ###
```python
{previous_code}
```
""".strip()



# -----------------------------------------------------------------------------
# Repair Agent
# -----------------------------------------------------------------------------


class Repair_Agent:

    def __init__(
        self,
        program: Program,
        output_file: str | Path,
        analysis_file: str | Path | None = None,
        llm: QwenLLM | None = None,
    ) -> None:
        self.program = program
        self.output_file = Path(output_file)
        self.analysis_file = Path(analysis_file) if analysis_file else None
        self.llm = llm or QwenLLM()
        self.num_tries = 0
        self.max_attempts = 5
        self.verbose = False
        self.conversation: list[dict] = []

    # -- single repair step ------------------------------------

    def _repair_step(self, analysis: dict[str, Any]) -> str:
        failing = analysis["failing_tests"]

        if self.num_tries == 0:
            user_message = build_repair_prompt(
                self.program.get_description(),
                self.program.get_student_code(),
                failing,
                analysis["suspicious_text"],
            )
        else:
            failing_section = f"The following tests still fail:\n{failing}\n" if failing else "Tests still fail.\n"
            user_message = f"{failing_section}Try again. Return ONLY the corrected Python code, no explanation."

        self.conversation.append({"role": "user", "content": user_message})

        if self.verbose:
            print(f"# Attempt {self.num_tries}")
            print(user_message)

        response = self.llm.generate_chat(self.conversation)
        self.conversation.append({"role": "assistant", "content": response})

        self.num_tries += 1

        if self.verbose:
            print("LLM response:\n", response)

        return _extract_code(response)

    # -- repair loop ------------------------------------

    def repair_loop(self) -> None:
        self.num_tries = 0
        self.conversation = []
        solved = False

        for _ in range(self.max_attempts):

            runner = FauxPyRunner(self.program)
            analysis = runner.get_analysis()

            # Syntax error: nothing FauxPy can do - stop immediately
            if analysis["has_syntax_error"]:
                break

            if not analysis["failing_tests"]:
                solved = True
                break

            repaired = self._repair_step(analysis)

            output_path = self.output_file.with_suffix(".py")
            output_path.write_text(repaired, encoding="utf-8")
            self.program.set_submission_path(output_path)



#ANALYSIS AND STATISTICS

        if self.analysis_file:
            statistics = {
                "submission": str(self.program.get_original_submission_path()),
                "solved": solved,
                "iterations": self.num_tries,
            }
       
            self.analysis_file.parent.mkdir(parents=True, exist_ok=True)
            with self.analysis_file.open("a", encoding="utf-8") as f:
                f.write(json.dumps(statistics) + "\n")
        return "DONE"





# -----------------------------------------------------------------------------
# Feedback Agent
# -----------------------------------------------------------------------------

class Feedback_Agent:
    def __init__(self,
        program: Program,
        llm: QwenLLM | None = None,
        analysis_file: str | Path | None = None,
        output_file: str | Path | None = None,
    ) -> None:
        self.program = program
        self.llm = llm or QwenLLM()
        self.analysis_file = Path(analysis_file) if analysis_file else None
        self.output_file = Path(output_file) if output_file else None

    def _base(self) -> tuple[str, str]:
        return self.program.get_description(), self.program.get_original_student_code()

    def _run_analysis(self) -> dict[str, Any]:
        return FauxPyRunner(self.program).get_analysis()

    def _edge_case_prompt(
        self,
        description: str,
        student_code: str,
        analysis: dict[str, Any],
    ) -> str | None:
        if not student_code.strip():
            return build_feedback_prompt_empty(description)
        if analysis.get("has_syntax_error"):
            return build_feedback_prompt_syntax_error(description, student_code, analysis["syntax_error"])
        return None

    def create_feedback_basic(self) -> str:
        """Type 1: description + student code only."""
        description, student_code = self._base()
        analysis = self._run_analysis()
        prompt = self._edge_case_prompt(description, student_code, analysis) or \
                 build_feedback_prompt_basic(description, student_code)
        return self.llm.generate(prompt)

    def create_feedback_with_tests(self) -> str:
        """Type 2: + failing tests. Falls back to basic if none available."""
        description, student_code = self._base()
        analysis = self._run_analysis()
        prompt = self._edge_case_prompt(description, student_code, analysis) or \
                 build_feedback_prompt_with_tests(description, student_code, analysis["failing_tests"])        
        return self.llm.generate(prompt)

    def create_feedback_with_localization(self) -> str:
        """Type 3: + FauxPy suspicious lines. Falls back to basic if none available."""
        description, student_code = self._base()
        analysis = self._run_analysis()
        prompt = self._edge_case_prompt(description, student_code, analysis) or \
                 build_feedback_prompt_with_localization(description, student_code, analysis["suspicious_text"])
        return self.llm.generate(prompt)

    def create_feedback_with_llm_localization(self) -> str:
        """Type 4: LLM identifies suspicious lines first, then gives feedback based on them."""
        description, student_code = self._base()
        analysis = self._run_analysis()
        edge = self._edge_case_prompt(description, student_code, analysis)
        if edge:
            return self.llm.generate(edge)
        loc_prompt = build_llm_localization_prompt(description, student_code, analysis["failing_tests"])
        suspicious_lines = self.llm.generate(loc_prompt)
        prompt = build_feedback_prompt_with_localization(description, student_code, suspicious_lines)
        return self.llm.generate(prompt)

    def create_feedback_with_repair(self, repaired_code: str | None = None) -> str:
        """Type 5: uses externally repaired code as reference. Falls back to basic if none provided."""
        description, student_code = self._base()
        analysis = self._run_analysis()
        edge = self._edge_case_prompt(description, student_code, analysis)
        if edge:
            return self.llm.generate(edge)
        prompt = build_feedback_prompt_with_repair(description, student_code, repaired_code)
        feedback = self.llm.generate(prompt)
        return f"==Repaired Code==\n{repaired_code}\n\n==Feedback==\n{feedback}"














# -----------------------------------------------------------------------------
# Entry point
# -----------------------------------------------------------------------------

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Condition 1 pipeline: FauxPy -> LLM feedback or repair"
    )
    parser.add_argument("--submission-path", required=True)
    parser.add_argument("--test-suite-path", required=False, default=None)
    parser.add_argument("--description-path", required=False, default=None)
    parser.add_argument("--output-file", required=False, default=None,
                        help="Where to write the repaired submission.")
    parser.add_argument("--feedback-file", required=False, default=None,
                        help="Where to write the feedback text.")
    parser.add_argument("--analysis-file", required=False, default=None,
                        help="Where to write the repair statistics (JSON Lines).")
    parser.add_argument("--feedback-type", required=False, default=None,
                        choices=["1", "2", "3", "4", "5"],
                        help="1=basic, 2=with tests, 3=FauxPy localization, 4=LLM localization, 5=with repair.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()

    program = Program(
        submission_path=args.submission_path,
        test_suite_path=args.test_suite_path,
        description_path=args.description_path,
    )

    llm = QwenLLM()
    agent = Feedback_Agent(program=program, llm=llm, analysis_file=args.analysis_file)

    if args.feedback_type == "5":
        Repair_Agent(program=program, output_file=args.output_file, llm=llm, analysis_file=args.analysis_file).repair_loop()
        repaired_code = program.get_student_code()
        feedback = agent.create_feedback_with_repair(repaired_code)
    elif args.feedback_type:
        feedback = {
            "1": agent.create_feedback_basic,
            "2": agent.create_feedback_with_tests,
            "3": agent.create_feedback_with_localization,
            "4": agent.create_feedback_with_llm_localization,
        }[args.feedback_type]()
    else:
        Repair_Agent(program=program, output_file=args.output_file, analysis_file=args.analysis_file).repair_loop()

    if args.feedback_type and args.feedback_file:
        Path(args.feedback_file).write_text(feedback, encoding="utf-8")
    if args.feedback_type:
        print(feedback)
