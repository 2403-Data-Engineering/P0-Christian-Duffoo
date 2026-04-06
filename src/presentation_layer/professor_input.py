from __future__ import annotations
from models.professor import Professor
from presentation_layer.regex_validation import RegexValidation
import service_layer.professor_service as professor_service
import service_layer.course_service as course_service


class ProfessorInput:

    sel = "Your Selection: "
    change = "Change this value to: "

    reg_name = RegexValidation.NAME.value
    reg_email = RegexValidation.EMAIL.value
    reg_year = RegexValidation.YEAR.value


    def create_new_professor(self):
        print("Please enter information for the new professor.")
        first_name: str = input("Enter a valid First Name: ")
        RegexValidation.validate_input(first_name, self.reg_name)
        last_name: str = input("Last Name: ")
        RegexValidation.validate_input(last_name, self.reg_name)
        department: str = input("Department: ")
        RegexValidation.validate_input(department, self.reg_name)
        email: str = input("Email (must be unique): ")
        RegexValidation.validate_input(email, self.reg_email)
        
        self.new_professor: Professor = Professor(None, first_name, last_name, department, email)
        professor_service.save_new_professor(self.new_professor)


    def update_existing_professor(self):
        id: str = input("Enter the unique professor ID of the professor you'd like to edit: ")
        selected_professor = professor_service.get_professor_from_id(id)
        print(selected_professor)
        print(f"""Please select what attribute you'd like to change about {selected_professor.first_name} {selected_professor.last_name}:
===============
1) First Name
2) Last Name
3) Department
4) Email
              """)
        
        user_attr: str = input(self.sel)
        while (user_attr) not in ["1", "2", "3", "4"]:
            user_attr: str = input("Invalid attribute value. Please try again: ")

        
        user_input: str = input(self.change)
        reg = None
        match user_attr:
            case "1":
                reg = self.reg_name
            case "2":
                reg = self.reg_name
            case "3":
                reg = self.reg_name
            case "4":
                reg = self.reg_email
        RegexValidation.validate_input(user_input, reg)
        #TODO: Implement regex class and use it to verify input

        professor_service.update_professor(selected_professor, user_attr, user_input)


    def professor_removal(self):
        id: str = input("Enter the unique Professor ID of the professor you're removing: ")
        selected_professor = professor_service.get_professor_from_id(id)
        print(selected_professor)
        print(f"""Would you like to remove {selected_professor.first_name} from the system?
1) Yes
2) No
              """)
        
        choice: str = input(self.sel)
        while choice not in ["1", "2"]:
            choice: str = input("Invalid option. Please try again: ")

        if choice == "1":
            ready_flag = professor_service.check_instructed_courses(selected_professor)
            if not ready_flag:
                professor_service.remove_professor(selected_professor)
            else:
                print("This professor is the instructor of one or more courses")
        else:
            print("Removal cancelled. Returning to professor management menu...")


    def generate_professor_report(self):
        id: str = input("Enter the unique Professor ID of the professor you'd like to generate a report for: ")
        selected_professor = professor_service.get_professor_from_id(id)
        print(f"Generating report for: {selected_professor.first_name} {selected_professor.last_name}...")
        filepath = professor_service.generate_report(selected_professor)

        return filepath