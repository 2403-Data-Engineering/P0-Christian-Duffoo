from abc import abstractmethod
#from typing import TYPE_CHECKING

from presentation_layer.student_input import StudentInput
import service_layer.student_service as student_service
from presentation_layer.professor_input import ProfessorInput
import service_layer.professor_service as professor_service
from presentation_layer.course_input import CourseInput
import service_layer.course_service as course_service

#if TYPE_CHECKING:
import presentation_layer.navigator as navigator


class Menu:

    def __init__(self, student_input: StudentInput, professor_input: ProfessorInput, course_input: CourseInput):
        self.student_input: StudentInput = student_input
        self.professor_input: ProfessorInput = professor_input
        self.course_input: CourseInput = course_input

    @abstractmethod
    def render() -> None:
        pass

    def go_to_main(self):
        navigator.navigate(MainMenu(self.student_input, self.professor_input, self.course_input))
    
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
                navigator.navigate(StudentMenu(self.student_input, self.professor_input, self.course_input))
            case "2":
                print("Entering the professor management system...")
                navigator.navigate(ProfessorMenu(self.student_input, self.professor_input, self.course_input))
            case "3":
                print("Entering the class management system...")
                navigator.navigate(ClassMenu(self.student_input, self.professor_input, self.course_input))
            case "0":
                navigator.quit_program(self)
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
                print("Viewing all students...\n(ID, First Name, Last Name, Email, Major, Year)")
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
                self.student_input.view_course_enrollment()
            case "8":
                filepath = self.student_input.generate_student_report()
                if filepath == None:
                    print("Invalid ID.")
                else:
                    print("Access your report at:", filepath)
                    print("NOTE: Generating a new student report will overwrite an existing report unless you move it from the repository or rename it.")
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
                self.professor_input.create_new_professor()
            case "2":
                print("Viewing all professors...\n(ID, First Name, Last Name, Department, Email)")
                professor_service.view_professors()
            case "3":
                print("Proceeding to update menu...")
                self.professor_input.update_existing_professor()
            case "4":
                print("Note: A professor can only be removed if they are not teaching any courses.")
                self.professor_input.professor_removal()
            case "5":
                filepath = self.professor_input.generate_professor_report()
                if filepath == None:
                    print("Invalid ID.")
                else:
                    print("Access your report at:", filepath)
                    print("NOTE: Generating a new professor report will overwrite an existing report unless you move it from the repository or rename it.")
            case "0":
                print(self.m_menu)
                self.go_to_main()
            case _:
                print(self.invalid)
                print(self.m_menu)
                

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
5) View enrolled students in a course
0) Return to Main Menu
              """)
        
        user_input: str = input(self.sel)
        match user_input:
            case "1":
                self.course_input.create_new_course()
            case "2":
                print("Viewing all currently active courses...\n(ID, Course Name, Assigned Professor ID)")
                course_service.view_courses()
            case "3":
                print("Proceeding to update menu...")
                self.course_input.update_existing_course()
            case "4":
                print("WARNING: Removing a course will also remove all of its enrollments")
                print("If you'd like to restore it later, you will have to enroll all its students again")
                self.course_input.course_removal()
            case "5":
                self.course_input.view_student_enrollment()
            case "0":
                print(self.m_menu)
                self.go_to_main()
            case _:
                print(self.invalid)
                print(self.m_menu)