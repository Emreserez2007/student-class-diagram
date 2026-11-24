# course.py
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from student import Student


class Course:
    def __init__(self, code: str, title: str):
        self._code = code
        self._title = title
        self._students: List[Student] = []

    def add_student(self, student: Student) -> None:
        if student not in self._students:
            self._students.append(student)
            student.enroll(self)

    @property
    def code(self) -> str:
        return self._code

    @property
    def title(self) -> str:
        return self._title

    @property
    def students(self) -> List[Student]:
        return self._students

    def __str__(self) -> str:
        return f"{self._code} - {self._title}"
