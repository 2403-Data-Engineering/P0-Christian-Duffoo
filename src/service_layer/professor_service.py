from models.student import Student
from models.professor import Professor
from models.course import Course

import data_layer.professor_dao as professor_dao

professor_smark = Professor("12", "Mark", "Smark", "Science", "mark.smark@emark.com")
professor_fisher = Professor("13", "Ashley", "Fisher", "Psychology", "ashley.fisher@school.edu")
professor_johnson = Professor("9", "Dwayne", "Johnson", "Electrical", "dwayne.johnson@wrestle.mania")

professor_list = [professor_smark, professor_fisher, professor_johnson]


def save_new_professor(professor: Professor):
    print(professor)
    try:
        professor_dao.save_professor(professor)
        print(f"Saved professor {professor.first_name} {professor.last_name} into the system!")
    except:
        print("There was an error in saving the new professor, likely due to duplicate email. Returning to professor management menu...")


def view_professors():
    result = professor_dao.view_all_professors()
    for row in result:
        value = list(row.values())
        print(value)


def update_professor(selected_professor: Professor, user_int: str, user_input: str):
    match user_int:
        case "1":
            attribute = "First Name"
            change = "first_name"
        case "2":
            attribute = "Last Name"
            change = "last_name"
        case "3":
            attribute = "Department"
            change = "department"
        case "4":
            attribute = "Email"
            change = "email"

    try:
        professor_dao.update_professor(selected_professor.professor_id, change, user_input)
    except:
        print("There was an error, likely due to invalid input.")
        return

    print(f"Professor {selected_professor.first_name} {selected_professor.last_name}'s attribute: {attribute} has been updated to {user_input}")


def remove_professor(selected_professor: Professor):
    try:
        professor_dao.drop_professor(selected_professor.professor_id)
        print(f"Removed professor: {selected_professor.first_name} {selected_professor.last_name} from the system.")
    except:
        print("There was an error in deleting this row. Returning to professor management menu...")
        return 


def get_professor_from_id(id: str):
    result = professor_dao.get_professor_by_id(int(id))
    return Professor(**result)


def check_instructed_courses(professor: Professor):
    result = professor_dao.count_rows(professor.professor_id)
    result = list(result.values())
    if result[0] == 0:
        return False
    return True


def generate_report(professor: Professor):
    filename = professor_dao.generate_report(professor)
    return filename
