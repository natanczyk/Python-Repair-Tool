import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from LLMs.llm import QwenLLM
from test_notebooks.main_pipeline_alfa import build_repair_prompt
from test_notebooks.main_pipeline_alfa import _extract_code
    

llm = QwenLLM()

description = """
Write the function soma_lista that receives a list of numbers and returns their sum.
You may not use the built-in sum() function.

Example:
soma_lista([1, 2, 3]) -> 6
soma_lista([]) -> 0
"""

student_code = """
def soma_lista(lst):
    total = 0
    for i in range(len(lst)):
        total = total + i
    return total
"""

failing_tests = """
soma_lista([1, 2, 3]) -> 6   (got 3)
soma_lista([10, 20]) -> 30   (got 1)
"""

suspicious_lines = """
Line 4: suspiciousness 1.0000
"""

prompt = build_repair_prompt(description, student_code, failing_tests, suspicious_lines)

print("=== answer === \n")


response = llm.generate(prompt)
response = _extract_cod