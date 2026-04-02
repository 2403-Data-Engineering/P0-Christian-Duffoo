from abc import abstractmethod
#from typing import TYPE_CHECKING


from presentation_layer.student_input import StudentInput
import service_layer.student_service as student_service

#if TYPE_CHECKING:
from presentation_layer.navigator import Navigator


class Menu:


    def __init__(self, navigator: Navigator, student_input: StudentInput):
        self.cursor: Navigator = navigator
        self.student_input: StudentInput = student_input

    @abstractmethod
    def render() -> None:
        pass

    def go_to_main(self):
        self.cursor.navigate(MainMenu(self.cursor, self.student_input))

    
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

        user_input: str = input(self.sel)
        match user_input:
            case "1":
                print("Entering the student management system...")
                self.cursor.navigate(StudentMenu(self.cursor, self.student_input))
            case "2":
                print("Entering the professor management system...")
                self.cursor.navigate(ProfessorMenu(self.cursor, self.student_input))
            case "3":
                print("Entering the class management system...")
                self.cursor.navigate(ClassMenu(self.cursor, self.student_input))
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
7) View student's enrollment
8) Generate Student Enrollment Report
0) Return to Main Menu         
              """)
        
        user_input: str = input(self.sel)
        match user_input:
            case "1":
                self.student_input.create_new_student()
            case "2":
                print("Viewing all students...")
                student_service.view_students()
            case "3":
                print("Proceeding to update menu...")
                self.student_input.update_existing_student()
            case "4":
                print("Note: A student can only be removed if they are not enrolled in any courses.")
                self.student_input.student_removal()
            case "5":
                self.student_input.enroll_student_in_course()
            case "6":
                print("WARNING: Dropping a student's enrollment does not have a confirmation. Ensure you have the right ID's")
                self.student_input.drop_student_from_course()
            case "7":
                self.student_input.view_student_enrollment()
            case "8":
                filepath = self.student_input.generate_student_report()
                print("Access your html report at: ", filepath)
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
                