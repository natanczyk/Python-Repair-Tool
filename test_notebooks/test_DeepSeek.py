from LLMs.llm import DeepSeekLLM

llm = DeepSeekLLM()

prompt = """
You are a debugging assistant.

Student code:
def is_even(n):
    return n % 2 == 1

Failing test:
assert is_even(4) == True

Explain the bug briefly.
"""

response = llm.generate(prompt)

print("\n=== RESPONSE ===")
print(response)