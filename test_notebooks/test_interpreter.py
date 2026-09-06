from Localization.interpreter import Interpreter

with open("Data/Assignment1/student1.py", "r", encoding="utf-8") as f:
    submission_code = f.read()

interpreter = Interpreter(
    expected_function_name="max_of_three",
    expected_params=["a", "b", "c"]
)

normalized_code = interpreter.normalize_code(submission_code)

print("=== NORMALIZED CODE ===")
print(normalized_code)

with open("Data/Assignment1/student1_normalized.py", "w", encoding="utf-8") as f:
    f.write(normalized_code)

print("Saved to student1_normalized.py")



#LAter: interpreter should read the task description and change the submission to the right format. 
# the parameters are given in the description and the function name is defined by the submission, for example LAB1ex04