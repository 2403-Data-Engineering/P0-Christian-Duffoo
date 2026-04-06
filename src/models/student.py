from dataclasses import dataclass


@dataclass
class Student:
    student_id: int
    first_name: str
    last_name: str
    email: str
    major: str
    school_year: str