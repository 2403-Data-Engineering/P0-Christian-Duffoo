import data_layer.course_dao as course_dao
from models.student import Student
from models.course import Course
from models.professor import Professor


def get_course_from_id(id: str):
    #TODO: Query database course table
    result = course_dao.get_course_by_id(int(id))
    return Course(**result)


def save_new_course(course: Course):
    print(course)
    print(f"New course: {course.course_name} has been created, with Professor {course.assigned_professor} assigned to it.")
        #This is a placeholder, will actually interact with database 
        #Ensure email is unique?
        #If new student is valid, enter it into sql student table
        #If invalid, return invalid message and do not insert
        #Put constraints on the sql table


def view_courses():
    #TODO: SELECT * from student table
    result = course_dao.view_all_courses()
    for row in result:
        value = list(row.values())
        print(value)

def update_course(selected_course: Course, user_int: str, user_input):
    #TODO: Updates selected_student (already confirmed to exist) attribute according to int
    #Database returns result and prompts what attribute to change
    #Perform update function


    match user_int:
        case "1":
            print(f"Course {selected_course.course_name} has been renamed to {user_input}")
        case "2":
            print(f"Course {selected_course.course_name}'s instructor has been changed. It is now taught by {user_input.first_name} {user_input.last_name}.")

def remove_course(course: Course):
    #TODO: Call database to remove row with student 
    print(f"Removed course {course.course_name} from the system.")
        
        #User enters student ID
        #Checks if student exists in table
        #Prevent removal if student is enrolled in a course
        #Have to remove enrollment junction from each class
        #Not necessarily drop row, but ignore it to keep data

def view_enrollment(course: Course):
    enrollment_list = ["12, John Smith", "19, Jane Doe", "7, Chris Duffoo"]
    #TODO: Check number of rows student has in enrollment table
    print(f"Students enrolled in {course.course_name}:")
    for enrollment in enrollment_list:
        print(enrollment)