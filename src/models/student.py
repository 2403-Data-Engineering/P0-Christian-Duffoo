from dataclasses import dataclass


@dataclass
class Student:
    student_id: str
    first_name: str
    last_name: str
    email: str
    major: str
    year: str