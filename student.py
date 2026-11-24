# student.py
from __future__ import annotations
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from course import Course


class Student:
    def __init__(self, student_id: int, name: str, email: str):
        self._student_id = student_id
        self._name = name
        self._email = email
        self._courses: List[Course] = []

    def enroll(self, course: Course) -> None:
        if course not in self._courses:
            self._courses.append(course)
            course.add_student(self)

    @property
    def student_id(self) -> int:
        return self._student_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def email(self) -> str:
        return self._email

    @property
    def courses(self) -> List[Course]:
        return self._courses

    def __str__(self) -> str:
        return f"{self._student_id} - {self._name}"
