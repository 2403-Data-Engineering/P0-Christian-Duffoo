from dataclasses import dataclass


@dataclass
class Professor:
    first_name: str
    last_name: str
    department: str
    email: str