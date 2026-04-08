import data_layer.course_dao as course_dao
from models.student import Student
from models.course import Course
from models.professor import Professor



def save_new_course(course: Course):
        prof_name = course_dao.save_course(course)
    
        print(f"New course: {course.course_name} has been created, with Professor {prof_name} assigned to it.")



def view_courses():
    result = course_dao.view_all_courses()
    for row in result:
        value = list(row.values())
        print(value)


def update_course(selected_course: Course, user_int: str, user_input):
    try:
        match user_int:
            case "1":
                course_dao.edit_course(selected_course.course_id, "course_name", user_input)
                print(f"Course {selected_course.course_name} has been renamed to {user_input}")
            case "2":
                course_dao.edit_course(selected_course.course_id, "prof_id", user_input.professor_id)
                print(f"Course {selected_course.course_name}'s instructor has been changed. It is now taught by {user_input.first_name} {user_input.last_name}.")
    except:
        print("There was an error in updating this course")
        return
                
            
def remove_course(course: Course):
    try:
        course_dao.drop_course(course.course_id)
        print(f"Removed course: {course.course_name} from the system.")
    except:
        print("There was an error in deleting this row. Returning to course management menu...")
        return 
        


def view_enrollment(course: Course):
    print(course)
    result = course_dao.view_enrollment(course.course_id)
    print(f"Here are the students enrolled in {course.course_name}\n(ID, First Name, Last Name)")
    for row in result:
        value = list(row.values())
        print(value)


def get_course_from_id(id: str):
    result = course_dao.get_course_by_id(int(id))
    return Course(**result)