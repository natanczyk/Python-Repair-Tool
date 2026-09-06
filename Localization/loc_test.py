
import subprocess
from pathlib import Path
import os
import pytest
import sys
import re


ASSIGNMENT_PATH = Path(r"D:\Master\MASTER_PROJECT\Data\assignment1")
file = "student1.py"


def run_fauxpy():
    cmd = [
        sys.executable, "-m", "pytest",
        str(ASSIGNMENT_PATH),
        "--src", str(ASSIGNMENT_PATH),
        "-s"  # 👈 VERY IMPORTANT (disables output capture)
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout + "\n" + result.stderr



def parse_suspisiousness(output):
    suspicious = []
    capture = False  # start capturing after header

    for line in output.splitlines():
        line = line.strip()

        
        if "Scores for Ochiai" in line:
            capture = True
            continue

        # Stop when table ends
        if capture and line.startswith("----"):
            continue
        if capture and line == "":
            break

        # Parse actual rows
        if capture and "|" in line and file in line:
            parts = line.split("|")

            try:
                line_number = int(parts[1].strip())
                score = float(parts[2].strip())

                suspicious.append({
                    "line": line_number,
                    "score": score
                })
            except:
                pass
            
    suspicious.sort(key=lambda x: x["score"], reverse=True)

    return suspicious



def get_suspicious_lines():
    Output = run_fauxpy()
    
    
    suspiciousness = parse_suspisiousness(Output)
    return suspiciousness

def format_incorrect_tests():
    Output = run_fauxpy()
    incorrect = [line for line in Output.splitlines() if line.startswith("FAILED")]

    if not incorrect:
        return "No failing tests were produced by FauxPy."

    formatted = []

    for line in incorrect:
        

        match = re.search(r"assert (.+) == (.+)", line)
        if match:
            actual = match.group(1).strip()
            expected = match.group(2).strip()

            formatted.append(
                f"Expected: {expected}, Actual: {actual}"
            )
        else:
            formatted.append(line)

    return "\n\n".join(formatted)




if __name__ == "__main__":
    result = get_suspicious_lines()
    failed = format_incorrect_tests()
    print(result)
    print(failed)












