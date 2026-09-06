from __future__ import annotations

from pathlib import Path


class Program:
    def __init__(
        self,
        submission_path: str | Path,
        test_suite_path: str | Path | None = None,
        description_path: str | Path | None = None,
    ) -> None:
        self.submission_path = Path(submission_path).resolve()
        self.original_submission_path = self.submission_path
        self.test_suite_path = Path(test_suite_path).resolve() if test_suite_path else None
        self.description_path = Path(description_path).resolve() if description_path else None

    def get_submission_path(self) -> Path:
        return self.submission_path

    def get_original_submission_path(self) -> Path:
        return self.original_submission_path

    def set_submission_path(self, new_path: str | Path) -> None:
        self.submission_path = Path(new_path).resolve()

    def get_test_suite_path(self) -> Path | None:
        return self.test_suite_path

    def get_description_path(self) -> Path | None:
        return self.description_path

    def get_original_student_code(self) -> str:
        return self.original_submission_path.read_text(encoding="utf-8")

    def get_student_code(self) -> str:
        return self.submission_path.read_text(encoding="utf-8")

    def get_description(self) -> str | None:
        if self.description_path is None:
            return None
        return self.description_path.read_text(encoding="utf-8")

    def get_test_suite_text(self) -> str | None:
        if self.test_suite_path is None:
            return None
        return self.test_suite_path.read_text(encoding="utf-8")
