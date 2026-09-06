"""
RepairAgent: four repair strategies for automated program repair.

Strategy        Oracle      Localization source
-----------     -------     -------------------
none            pytest      none
fauxpy          FauxPy      FauxPy Ochiai scores (updated each iteration)
best_loc        pytest      Gemma4 pre-computed suspicious lines (static)
self_llm        pytest      Same LLM localizes (updated each iteration)
"""
from __future__ import annotations

import re
import shutil
import tempfile
from pathlib import Path
from typing import Any

from Localization.fauxpy_runner import FauxPyRunner
from Localization.program import Program
from repair_research.prompts import (
    build_followup_prompt,
    build_localization_prompt,
    build_repair_prompt,
)
from repair_research.test_runner import run_tests


def _extract_code(response: str) -> str:
    match = re.search(r"```(?:python)?\n(.*?)```", response, re.DOTALL)
    if match:
        return match.group(1).strip()
    return response.strip()


class RepairAgent:
    def __init__(
        self,
        program: Program,
        llm: Any,
        work_dir: Path,
        max_attempts: int = 4,
    ) -> None:
        self.program = program
        self.llm = llm
        self.work_dir = Path(work_dir)
        self.max_attempts = max_attempts

        # populated after calling a repair method
        self.solved: bool = False
        self.iterations: int = 0
        self.final_code: str | None = None

        self._conversation: list[dict] = []

    # ── internal helpers ──────────────────────────────────────────────────────

    def _reset(self) -> None:
        self.solved = False
        self.iterations = 0
        self.final_code = None
        self._conversation = []
        self.program.set_submission_path(self.program.get_original_submission_path())

    def _save_repair(self, code: str) -> None:
        out = self.work_dir / self.program.get_original_submission_path().name
        out.write_text(code, encoding="utf-8")
        self.program.set_submission_path(out)

    def _llm_step(self, prompt: str) -> str:
        self._conversation.append({"role": "user", "content": prompt})
        response = self.llm.generate_chat(self._conversation)
        self._conversation.append({"role": "assistant", "content": response})
        return _extract_code(response)

    def _build_prompt(
        self, failing_hint: str, suspicious_lines: str | None = None
    ) -> str:
        if self.iterations == 0:
            return build_repair_prompt(
                self.program.get_description(),
                self.program.get_student_code(),
                failing_hint,
                suspicious_lines,
            )
        return build_followup_prompt(failing_hint, suspicious_lines)

    def _finalize(self) -> None:
        if self.solved:
            self.final_code = self.program.get_student_code()
        else:
            self.final_code = None

    # ── public repair methods ─────────────────────────────────────────────────

    def repair_none(self) -> None:
        """Repair loop with no localization information."""
        self._reset()

        for _ in range(self.max_attempts):
            result = run_tests(
                self.program.get_submission_path(),
                self.program.get_test_suite_path(),
            )
            if result["timed_out"]:
                break
            if result["has_syntax_error"]:
                failing_hint = result["syntax_error_msg"]
            elif result["solved"]:
                self.solved = True
                break
            else:
                failing_hint = result["failing_tests"]

            code = self._llm_step(self._build_prompt(failing_hint))
            self._save_repair(code)
            self.iterations += 1

        self._finalize()

    def repair_fauxpy(self) -> None:
        """Repair loop using FauxPy Ochiai scores at each iteration."""
        self._reset()

        for _ in range(self.max_attempts):
            runner = FauxPyRunner(self.program)
            analysis = runner.get_analysis()

            if analysis["timed_out"]:
                break
            if analysis["has_syntax_error"]:
                failing_hint = analysis["output"]
                suspicious_lines = None
            elif not analysis["failing_tests"]:
                self.solved = True
                break
            else:
                failing_hint = analysis["failing_tests"]
                suspicious_lines = analysis["suspicious_text"]

            code = self._llm_step(self._build_prompt(failing_hint, suspicious_lines))
            self._save_repair(code)
            self.iterations += 1

        self._finalize()

    def repair_best_loc(self, loc_llm: Any) -> None:
        """Repair loop where Gemma4 (loc_llm) localizes and the repair LLM fixes.
        Localization runs on the current code at each iteration."""
        self._reset()

        for _ in range(self.max_attempts):
            result = run_tests(
                self.program.get_submission_path(),
                self.program.get_test_suite_path(),
            )
            if result["timed_out"]:
                break
            if result["has_syntax_error"]:
                failing_hint = result["syntax_error_msg"]
                suspicious_lines = None
            elif result["solved"]:
                self.solved = True
                break
            else:
                failing_hint = result["failing_tests"]
                loc_prompt = build_localization_prompt(
                    self.program.get_student_code(), failing_hint
                )
                suspicious_lines = loc_llm.generate(loc_prompt)

            code = self._llm_step(self._build_prompt(failing_hint, suspicious_lines))
            self._save_repair(code)
            self.iterations += 1

        self._finalize()

    def repair_self_llm(self) -> None:
        """Repair loop where the same LLM localizes then repairs at each iteration."""
        self._reset()

        for _ in range(self.max_attempts):
            result = run_tests(
                self.program.get_submission_path(),
                self.program.get_test_suite_path(),
            )
            if result["timed_out"]:
                break
            if result["has_syntax_error"]:
                failing_hint = result["syntax_error_msg"]
                suspicious_lines = None
            elif result["solved"]:
                self.solved = True
                break
            else:
                failing_hint = result["failing_tests"]
                loc_prompt = build_localization_prompt(
                    self.program.get_student_code(), failing_hint
                )
                suspicious_lines = self.llm.generate(loc_prompt)

            code = self._llm_step(self._build_prompt(failing_hint, suspicious_lines))
            self._save_repair(code)
            self.iterations += 1

        self._finalize()
