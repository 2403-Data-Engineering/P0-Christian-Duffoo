from dataclasses import dataclass


@dataclass
class Course:
    course_id: int
    course_name: str
    assigned_professor: str
    prof_id: int