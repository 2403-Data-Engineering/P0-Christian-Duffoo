from __future__ import annotations
from models.course import Course
from presentation_layer.regex_validation import RegexValidation
import service_layer.course_service as course_service
import service_layer.professor_service as professor_service
import service_layer.student_service as student_service

class CourseInput:
    sel = "Your Selection: "
    change = "Change this value to: "

    reg_name = RegexValidation.NAME.value
    
    def create_new_course(self):
        print("Please enter information for the new course.")
        course_name: str = input("Enter a valid CourseName: ")
        RegexValidation.validate_input(course_name, self.reg_name)
        prof_id: str = input("Enter the Professor ID of the professor to be assigned to this course: ")
        assigned_professor = professor_service.get_professor_from_id(prof_id)

        self.new_course: Course = Course(None, course_name, assigned_professor.last_name, prof_id)
        course_service.save_new_course(self.new_course)


    def update_existing_course(self):
        id: str = input("Enter the unique course ID of the course you'd like to edit: ")
        selected_course = course_service.get_course_from_id(id)
        print(selected_course)
        print(f"""Please select what attribute you'd like to change about {selected_course.course_name}:
===============
1) Course Name
2) Assigned Professor ID
              """)
        
        user_attr: str = input(self.sel)
        while (user_attr) not in ["1", "2"]:
            user_attr: str = input("Invalid attribute value. Please try again: ")

        
        user_input = None
        match user_attr:
            case "1":
                user_input: str = input(self.change)
                RegexValidation.validate_input(user_input, self.reg_name)
            case "2":
                temp_input: str = input("Enter the professor ID of the new professor you'd like to assign to this course: ")
                user_input = professor_service.get_professor_from_id(temp_input)


        course_service.update_course(selected_course, user_attr, user_input)


    def course_removal(self):
        id: str = input("Enter the unique course ID of the course you're removing: ")
        selected_course = course_service.get_course_from_id(id)
        print(selected_course)
        print(f"""Would you like to remove {selected_course.course_name} from the system?
1) Yes
2) No
              """)
        
        choice: str = input(self.sel)
        while choice not in ["1", "2"]:
            choice: str = input("Invalid option. Please try again: ")

        if choice == "1":
                course_service.remove_course(selected_course)
        else:
            print("Removal cancelled. Returning to course management menu...")

    def view_student_enrollment(self):
        id: str = input("Enter the unique course ID of the course you'd like to view the enrollment for: ")
        selected_course = course_service.get_course_from_id(id)

        course_service.view_enrollment(selected_course)