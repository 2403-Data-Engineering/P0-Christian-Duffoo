from models.student import Student
from models.course import Course

course_math = Course("101", "Math", "John Smith")
course_cs = Course("404", "Python", "Kyle Plummer")
course_history = Course("225", "American History", "Jane Doe")

def get_course_from_id(id: str):
    #TODO: Query database course table
    return course_math