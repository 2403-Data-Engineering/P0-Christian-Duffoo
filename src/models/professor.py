from dataclasses import dataclass


@dataclass
class Professor:
    staff_id: int
    first_name: str
    last_name: str
    department: str
    email: str