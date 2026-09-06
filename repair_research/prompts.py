from __future__ import annotations


def build_repair_prompt(
    description: str | None,
    code: str,
    failing_hint: str,
    suspicious_lines: str | None = None,
) -> str:
    parts = [
        "You are an expert Python programmer. Fix the buggy program so that all tests pass.",
        "Return ONLY the corrected Python code inside a ```python ... ``` block.",
    ]
    if suspicious_lines:
        parts += ["\n### Suspicious Lines (fault localization)", suspicious_lines]
    if description:
        parts += ["\n### Assignment", description.strip()]
    parts += [f"\n### Buggy Code\n```python\n{code}\n```"]
    parts += [f"\n### Failing Tests\n{failing_hint}"]
    return "\n".join(parts).strip()


def build_followup_prompt(failing_hint: str, suspicious_lines: str | None = None) -> str:
    parts = ["The repaired code still fails. Here are the remaining failures:"]
    if suspicious_lines:
        parts += ["\n### Suspicious Lines", suspicious_lines]
    parts += [f"\n### Remaining Failing Tests\n{failing_hint}"]
    parts += ["\nReturn ONLY the corrected Python code inside a ```python ... ``` block."]
    return "\n".join(parts).strip()


def build_localization_prompt(code: str, failing_hint: str) -> str:
    return (
        "You are a fault localization expert for Python programs.\n"
        "The program below fails some tests. Identify the line numbers most likely to contain the bug and then order them from most to least suspicious.\n"
        f"\n### Code\n```python\n{code}\n```"
        f"\n\n### Failing Tests\n{failing_hint}"
        "\n\nReturn only the suspicious lines in the following format:\n"
        "Buggy lines: <line_number_1>, <line_number_2>, ...\n"
    ).strip()
