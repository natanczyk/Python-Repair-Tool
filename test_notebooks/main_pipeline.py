from __future__ import annotations

import argparse
import json
import tempfile
from pathlib import Path
from typing import Any

from LLMs.llm import DeepSeekLLM
from Localization.fauxpy_runner import FauxPyRunner
from Localization.program import Program
        
        
        
        
        

        
class Repair_Agent:
    """
    Condition 1: FauxPy + LLM Feedback-Only
    """

    def __init__(
        self,
        program: Program,
        output_file: str | Path,
        llm: DeepSeekLLM | None = None,
        
    ) -> None:
        self.program = program
        self.output_file = Path(output_file)
        self.llm = llm or DeepSeekLLM() #I want to change it to the latest model of QWEN with similar amount of parameters so my computer can handle it.
        self.num_tries = 0
        self.max_attempts = 5
        self.verbose=False



# I want three type of functions for creating the prompts:
# 1) the first one is a prompt to generate the feedback. It will have two versions: generic feedback based on description and student solution, and feedback based on description, repaired fauxpy-driven solution and student original submission.
# 2) the second one is a prompt for the first repair attempt and it will have two options: prompt for the fauxpy oriented repair which takes into consideration the suspicious lines and failing tests, and prompt for the normal llm repair which will not see the suspicious lines.
# 3) the third one is a prompt for the next repair attempts, which will take into consideration the previous incorrect repair, and will also have two options: with localization and without it.
# So three functions in total with clever if statements to generate the right prompt based on the conditions.



    def create_feedback(self) -> dict[str, Any]:
        assignment_text = self.program.get_description()
        student_code = self.program.get_student_code()
        runner = FauxPyRunner(self.program)
        analysis = runner.get_analysis()
        prompt = f"""
You are an educational Python debugging assistant.

Your task is to help a novice student understand the bug in their code.
Use the suspicious lines as guidance, but do not mention suspiciousness scores.
Do not give the full corrected solution.

Assignment:
{assignment_text}

Student code:
{student_code}

Failing tests / output:
{analysis["failing_tests"]}

Suspicious lines:
{analysis["suspicious_text"]}

Provide:
1. A brief explanation of the likely bug
2. A hint focused on the suspicious region

- Do NOT write code
- Do NOT show full solution
- Do NOT include test cases
- Do NOT include markdown or code blocks
""".strip()

        feedback = self.llm.generate(prompt)

        return {
            "assignment_text": assignment_text,
            "student_code": student_code,
            "feedback": feedback,
        }
        
     
        
        
     
        
        
        
        
        
        
        
        
# REPAIR AGENT (not fully implemented yet, but will be used in future conditions)
        
    def create_prompt(self, forwarded_analysis) -> str:
        student_code = self.program.get_student_code()
        assignment_text = self.program.get_description()
        
        analysis=forwarded_analysis


        prompt = f"""
    Fix all semantic bugs in the buggy Python program below.
    Focus especially on the suspicious region identified by fault localization.
    Modify the code as little as possible.
    Return ONLY the corrected Python code.
    Do not provide any explanation.

    ### Problem Description ###
    {assignment_text}

    ### Failing Tests / Output ###
    {analysis["failing_tests"]}

    ### Suspicious Lines ###
    {analysis["suspicious_text"]}

    ### Buggy Program <python> ###
    ```python
    {student_code}""".strip()
    
        return prompt
    
    
    
    
    
    def create_response(self, forwarded_analysis) -> str:
        assignment_text = self.program.get_description()
        analysis = forwarded_analysis
        

        prompt = f"""
### Feedback ###
Your previous repair was incorrect. Try again.
Fix the program by modifying it as little as possible.
Return ONLY the corrected Python code.
Do not provide any explanation.

### Problem Description ###
{assignment_text}

### Failing Tests / Output ###
{analysis["failing_tests"]}

### Suspicious Lines ###
{analysis["suspicious_text"]}

### Previous Incorrect Repair <python> ###
```python
{self.program.get_student_code()}""".strip()
        return prompt






    def repair_NO_localization(self, analysis) -> str:
        
        
        # THis loop will work almost the same but while repairing the code, we will not give the information about suspicious lines to the LLM,
        # so it will have to figure out the bug without any guidance.
        # The prompt will be almost the same, but wont have the suspicious lines part. (For example, if the loc=False , we will skip the suspiciousness part in the prompt generation).





    def repair(self, analysis) -> str:

        if self.num_tries == 0:
            prompt = self.create_prompt(analysis)
        else:
            prompt = self.create_response(analysis)

        if self.verbose:
            print(f"# Attempt = {self.num_tries}")
            print("\nPrompt:\n")
            print(prompt)
            print()

        response = self.llm.generate(prompt)
        #SHOULD BE IN STR FORMAT, ONLY CODE, NO EXPLANATION
        #I need formatting to the .py file there
        
        self.num_tries += 1

        if self.verbose:
            print("LLM response:\n")
            print(response)                    

        return response
    
    
    
    
    
    def repair_loop(self):
        
        for _ in range(self.max_attempts):
        
# Also it is possible that the student submission will by syntatically incorrect thus all test suites will fail. Is there a simple solution to this problem?

            runner = FauxPyRunner(self.program)
            analysis = runner.get_analysis()

            if analysis["failing_tests"]:

                repaired = self.repair(analysis)

                output_path = self.output_file.with_suffix(".py")
                output_path.write_text(repaired, encoding="utf-8")

                self.program.set_submission_path(output_path)

            else:
                
                print("No failing tests detected. Stopping repair loop.")
                break
        # in the analysis file we want to save 1) if the repair was successful or not
        # 2) how many iterations it took to get there
        # 3)length of the solution to see how invasive the repair was
        
        # I WANT TO SAVE the resuls FOR BOTH repair and repair_NO_localization, to be able to compare them later on. I will save it in a json file, which will be used for the analysis of the results later on. 
        # I will also save the final repaired code WITH localization, to be able to generate feedback for students on top of it.
    

        
                
                
                
                
            
class Feedback_Agent:
    def __init__(self, program: Program, llm: DeepSeekLLM | None = None) -> None:
        self.program = program
        self.llm = llm or DeepSeekLLM()
    # if interpreter is None, we will generate the feedback without the repair loop, so we will not be able to give the feedback based on the repaired code,
    # but only based on the original student submission and description.
    # I have to create a prompt for this type of feedback.
    # else we will generate two types of feedback: based on repair loop and without it.
    
    
    def create_feedback_with_repair(self, analysis) -> str:
        # Takes the student submission, description, and the repaired code, create the feedback out of this.
        #  I need to create the prompt for this type of feedback, which will be used in the LLM to generate the feedback.
        
    def create_feedback_NO_repair(self, analysis) -> str:
        # Takes the student submission and description, create the feedback out of this. 
        # create the prompt for this type of feedback, which will be used in the LLM to generate the feedback.





def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Condition 1 pipeline: FauxPy -> LLM feedback"
    )
    parser.add_argument("--assignment-path", required=True)
    parser.add_argument("--description-filename", required=False)
    parser.add_argument("--submission-path", required=True)
    parser.add_argument("--test-suite-filename", required=False)
    parser.add_argument("--output-file", required=False, default=r"Data\students\code1TEST.py")
    parser.add_argument("--json", action="store_true")
    return parser.parse_args()

# We should also pass here the file where the analysis will be stored


if __name__ == "__main__":
    args = parse_args()

    program = Program(
        assignment_path=args.assignment_path,
        submission_path=args.submission_path,
        description_filename=args.description_filename,
        test_suite_filename=args.test_suite_filename,
    )
    # if there is no test suite file its because apparently in this exercise the output is not dependent on the input, there is no need to run the tests, so we dont need interpreter.
    # IF there is a corresponding test suite, we will create the interpreter, else, interpreter = None.
    # interpreter = Interpreter()
    # if there is a corresponding test suite for the assignment, we will interpret the student submission.
    # But if there is no test suite it means we will not be able to run the tests and get the suspicious lines and we will just give the feedback based on the description and student submission, NO repair loop.

    pipeline = Repair_Agent(program=program, output_file=args.output_file)
    result = pipeline.create_feedback()

    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print("\n=== Feedback ===")
        print(result["feedback"])