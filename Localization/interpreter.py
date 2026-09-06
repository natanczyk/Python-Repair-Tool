from pathlib import Path
from typing import List



# Takes the description of the assignment, which indicates the variables 
# A student has to use (they will be probably saved as variables -> x, y), 
# The student also has to save the result in result or RESULT variable (because the result will indicate what to return). 
# A function name will be indicated in description file name (for example "l2ex5" or "l4e1"). 
# input to this class will be also the student submission.
# NOW the interpreter file will be used to take student code and change it to .py format readible for test suits, dress it in a function with appropiate name, used variables and return

class Interpreter:
    def __init__(self, function_name: str, inputs: List[str], output: str = "result"):

