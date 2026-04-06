from __future__ import annotations
from models.student import Student
from presentation_layer.regex_validation import RegexValidation
import service_layer.student_service as student_service
import service_layer.course_service as course_service



class StudentInput:

    sel = "Your Selection: "
    change = "Change this value to: "

    reg_name = RegexValidation.NAME.value
    reg_email = RegexValidation.EMAIL.value
    reg_year = RegexValidation.YEAR.value
    

    def create_new_student(self):
        print("Please enter information for the new student.")
        first_name: str = input("Enter a valid First Name: ")
        RegexValidation.validate_input(first_name, self.reg_name)
        last_name: str = input("Last Name: ")
        RegexValidation.validate_input(last_name, self.reg_name)
        email: str = input("Email (must be unique): ")
        RegexValidation.validate_input(email, self.reg_email)
        major: str = input("Major: ")
        RegexValidation.validate_input(major, self.reg_name)
        year = input("Year: ").lower()
        RegexValidation.validate_input(year, self.reg_year)

        self.new_student: Student = Student(None, first_name, last_name, email, major, year)
        student_service.save_new_student(self.new_student)


    def update_existing_student(self):
        id: str = input("Enter the unique Student ID of the student you'd like to edit: ")
        try:
            selected_student = student_service.get_student_from_id(id)
        except:
            print("Invalid ID")
            return
        
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
        while (user_attr) not in ["1", "2", "3", "4", "5"]:
            user_attr: str = input("Invalid attribute value. Please try again: ")

        user_input: str = input(self.change)
        reg = None
        match user_attr:
            case "1":
                reg = self.reg_name
            case "2":
                reg = self.reg_name
            case "3":
                reg = self.reg_email
            case "4":
                reg = self.reg_name
            case "5":
                user_input = user_input.lower()
                reg = self.reg_year
        RegexValidation.validate_input(user_input, reg)
        #TODO: Implement regex class and use it to verify input

        student_service.update_student(selected_student, user_attr, user_input)


    def student_removal(self):
        id: str = input("Enter the unique Student ID of the student you're removing: ")
        try:
            selected_student = student_service.get_student_from_id(id)
        except:
            print("Invalid ID.")
            return
        print(selected_student)
        print(f"""Would you like to remove {selected_student.first_name} from the system?
1) Yes
2) No
              """)
        
        choice: str = input(self.sel)
        while choice not in ["1", "2"]:
            choice: str = input("Invalid option. Please try again: ")

        if choice == "1":
            ready_flag = student_service.check_enrollment(selected_student)
            if not ready_flag:
                student_service.remove_student(selected_student)
            else:
                print(f"This student ({selected_student.first_name} {selected_student.last_name}) is enrolled in one or more courses and cannot be removed.")
        else:
            print("Removal cancelled. Returning to student management menu...")
        
        
    def enroll_student_in_course(self):
        try:
            id: str = input("Enter the unique Student ID of the student you're enrolling in a course: ")
            selected_student = student_service.get_student_from_id(id)
            course_id: str = input("Enter the course ID of the class you'd like to enroll this student in: ")
            selected_course = course_service.get_course_from_id(course_id)
        except:
           print("Invalid student or course ID")
           return

        student_service.enroll_student(selected_student, selected_course)


    def drop_student_from_course(self):
        try:
            id: str = input("Enter the unique Student ID of the student you're dropping from a course: ")
            selected_student = student_service.get_student_from_id(id)
            course_id: str = input("Enter the course ID of the class you'd like to drop this student from: ")
            selected_course = course_service.get_course_from_id(course_id)
        except:
            print("Invalid ID")
            return

        student_service.drop_student(selected_student, selected_course)


    def view_course_enrollment(self):
        id: str = input("Enter the unique Student ID of the student you'd like to view the enrollment for: ")
        try:
            selected_student = student_service.get_student_from_id(id)
        except:
            print("Invalid student ID.")
            return
        
        student_service.view_enrollment(selected_student)


    def generate_student_report(self):
        id: str = input("Enter the unique Student ID of the student you'd like to generate a report for: ")
        try:
            selected_student = student_service.get_student_from_id(id)
        except:
            print("Invalid ID")
            return
        print(f"Generating report for: {selected_student.first_name} {selected_student.last_name}...")
        filepath = student_service.generate_report(selected_student)

        return filepath