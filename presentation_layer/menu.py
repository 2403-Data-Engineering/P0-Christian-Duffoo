from __future__ import annotations
from abc import abstractmethod
from typing import TYPE_CHECKING

from service_layer.student_service import StudentService

if TYPE_CHECKING:
    from presentation_layer.navigator import Navigator

class Menu:
    def __init__(self, navigator: Navigator):
        self.cursor: Navigator = navigator

    @abstractmethod
    def render() -> None:
        pass


class MainMenu(Menu):

    def render(self):
        print("""
==========================================================================
Welcome to the administrator portal for college registration!
Please enter the number corresponding to the action you'd like to perform:
              
1) Manage Students
2) Manage Professors
3) Manage Classes
0) Finish and End Program      
        """)
    
        user_input: str = input()
        match user_input:
            case "1":
                print("Entering the student management system...")
                self.cursor.navigate(StudentMenu(self.cursor))
            case "2":
                print("Entering the professor management system...")
                self.cursor.navigate(ProfessorMenu(self.cursor))
            case "3":
                print("Entering the class management system...")
                self.cursor.navigate(ClassMenu(self.cursor))
            case "0":
                self.cursor.quit_program()
            case _:
                print("Invalid command. Please select one of the numbered options")
                

class StudentMenu(Menu):

    def render(self):
        print("""
======================================================
This is the menu to manage students at the university.
Please select your desired option:
              
1) Add new student to system
2) View all students
3) Update existing student's information
4) Remove student from system
5) Enroll student in course
6) Drop student from course
7) Generate Student Enrollment Report
0) Return to Main Menu         
              """)
        
        user_input: str = input()
        match user_input:
            case "1":
                print("Performing Operation...")
            case "0":
                self.cursor.navigate(MainMenu(self.cursor))


class ProfessorMenu(Menu):
    def render(self):
        print("""
================================================
This is the menu to manage employeed professors.
Please select your desired option:
              
1) Add new professor to system
2) View all professors
3) Update existing professor's information
4) Remove professor from system
5) Generate Professor Summary Report
0) Return to Main Menu
              """)
        
        user_input: str = input()
        match user_input:
            case "1":
                print("Performing Operation...")
            case "0":
                self.cursor.navigate(MainMenu(self.cursor))
    

class ClassMenu(Menu):
    def render(self):
        print("""
======================
This is the menu to manage courses.
Please select your desired option:
              
1) Add new course
2) View all active courses
3) Edit details of existing course
4) Remove course from system
5) View enrolled students in a class
0) Return to Main Menu
              """)
        
        user_input: str = input()
        
        match user_input:
            case "1":
                print("Performing Operation...")
            case "0":
                self.cursor.navigate(MainMenu(self.cursor))
    