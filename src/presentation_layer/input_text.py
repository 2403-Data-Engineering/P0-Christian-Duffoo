from __future__ import annotations
import re
from models.student import Student
from enum import Enum
import service_layer.student_service as student_service


class RegexValidation(Enum):
    def validate_input(input: str, regex: str) -> bool:
        #insert regex for non key related constraints, alongside class containing each type of validator
        #email, name, year
        return True


class InputText():

    sel = "Your Selection: "
    change = "Change this value to: "
    
    def create_new_student(self):
        print("Please enter information for the new student.")
        first_name: str = input("First Name: ")
        last_name: str = input("Last Name: ")
        email: str = input("Email (must be unique): ")
        major: str = input("Major: ")
        year = input("Year (Integer): ")

        self.new_student: Student = Student(None, first_name, last_name, email, major, year)
        student_service.save_new_student(self.new_student)


    def update_existing_student(self):
        id: str = input("Enter the unique Student ID of the student you wish to edit: ")
        selected_student = student_service.get_student_from_id(id)
        print(selected_student)
        print(f"""Please select what attribute you'd like to change about {selected_student.first_name} {selected_student.last_name}:
===============
1) First Name
2) Last Name
3) Email
4) Major
5) Year
              """)
        
        user_attr: str = input(self.sel)
        
        user_input: str = input(self.change)
        reg = ""
        RegexValidation.validate_input(user_input, reg)

        student_service.update_student(selected_student, user_attr, user_input)




