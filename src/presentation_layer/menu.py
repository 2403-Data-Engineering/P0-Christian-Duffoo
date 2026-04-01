from abc import abstractmethod
from typing import TYPE_CHECKING
from presentation_layer.input_text import InputText

import service_layer.student_service as student_service

#if TYPE_CHECKING:
from presentation_layer.navigator import Navigator



class Menu:


    def __init__(self, navigator: Navigator, input_text: InputText):
        self.cursor: Navigator = navigator
        self.input_text: InputText = input_text

    @abstractmethod
    def render() -> None:
        pass

    def go_to_main(self):
        self.cursor.navigate(MainMenu(self.cursor, self.input_text))

    
    sel = "Your Selection: "
    invalid = "Invalid command. Please select one of the numbered options."
    m_menu = "Returning to Main Menu..."


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
                self.cursor.navigate(StudentMenu(self.cursor, self.input_text))
            case "2":
                print("Entering the professor management system...")
                self.cursor.navigate(ProfessorMenu(self.cursor, self.input_text))
            case "3":
                print("Entering the class management system...")
                self.cursor.navigate(ClassMenu(self.cursor, self.input_text))
            case "0":
                self.cursor.quit_program()
            case _:
                print(self.invalid)
                

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
        
        user_input: str = input(self.sel)
        match user_input:
            case "1":
                self.input_text.create_new_student()
            case "2":
                print("Viewing all students...")
                print(self.m_menu)
                self.go_to_main()
            case "3":
                print("Proceeding to update menu...")
                self.input_text.update_existing_student()
            case "0":
                print(self.m_menu)
                self.go_to_main()
            case _:
                print(self.invalid)
                print(self.m_menu)

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
        
        user_input: str = input(self.sel)
        match user_input:
            case "1":
                print("Performing Operation...")
                
            case "0":
                print(self.m_menu)
                self.go_to_main()
            case _:
                print(self.invalid)
                

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
        
        
        
        user_input: str = input(self.sel)
        match user_input:
            case "1":
                print("Performing Operation...")
                print(self.m_menu)
            case "0":
                print(self.m_menu)
                self.go_to_main()
            case _:
                print(self.invalid)
                