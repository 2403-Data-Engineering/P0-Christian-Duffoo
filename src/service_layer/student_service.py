import data_layer.student_dao as student_dao
from models.student import Student
from models.course import Course

student_john = Student("20", "John", "Smith", "smith@john.com", "CS", "Freshman")
student_jane = Student("21", "Jane", " Doe", "jane.doe@school.edu", "Math", "Junior")
student_chris = Student("22", "Chris", "Duffoo", "chris.duffoo@college.net", "ECE", "Senior")

student_list = [student_john, student_jane, student_chris]

#DONE
def save_new_student(new_student: Student):
    try:
        student_dao.save_student(new_student)
        print(f"Saved student {new_student.first_name} {new_student.last_name} into the system!")
    except:
       print("There was an error in saving the new student, likely due to duplicate email. Returning to student management menu...")


#DONE
def view_students():
    result = student_dao.view_all_students()
    for row in result:
        value = list(row.values())
        print(value)


#DONE
def update_student(selected_student: Student, user_int: str, user_input: str):
    match user_int:
        case "1":
            attribute = "First Name"
            change = 'first_name'
        case "2":
            attribute = "Last Name"
            change = 'last_name'
        case "3":
            attribute = "Email"
            change = 'email'
        case "4":
            attribute = "Major"
            change = 'major'
        case "5":
            attribute = "Year"
            change = 'school_year'
    try:
        student_dao.update_student(selected_student.student_id, change, user_input)
    except:
        print("There was an error, likely due to invalid input.")
        return

    print(f"Student {selected_student.first_name} {selected_student.last_name}'s attribute: {attribute} has been updated to {user_input}")


#DONE
def remove_student(selected_student: Student):
    try:
        student_dao.drop_student(selected_student.student_id)
        print(f"Removed student: {selected_student.first_name} {selected_student.last_name} from the system.")
    except:
        print("There was an error in deleting this row. Returning to student management menu...")
        return


#DONE
def enroll_student(student: Student, course: Course):
    try:
        student_dao.enroll_student_in_course(student.student_id, course.course_id)
    except:
        print("Error occurred. This is likely due to a duplicate entry.")
        return
    print(f"Enrolled student {student.first_name} {student.last_name} into {course.course_name}.")


#DONE
def drop_student(student: Student, course: Course):
    #TODO: Drop row from enrollment table
    try:
        student_dao.drop_student_from_course(student.student_id, course.course_id)
    except:
        print("Error occurred. This enrollment likely does not exist")
        return
    
    print(f"Dropped student {student.first_name} {student.last_name} from {course.course_name}")
    #First checks if student exists in course
    #Ignores row instead of deleting row?


#DONE
def get_student_from_id(id: str):
    result = student_dao.get_student_by_id(int(id))
    return Student(**result)


#DONE
def check_enrollment(selected_student: Student):
    result = student_dao.count_rows(selected_student.student_id)
    result = list(result.values())
    if result[0] == 0:
        return False
    return True


#DONE
def view_enrollment(student: Student):
    print(student)
    result = student_dao.view_enrollment(student.student_id)
    print(f"Here are the courses {student.first_name} {student.last_name} is enrolled in:")
    for row in result:
        value = list(row.values())
        print(value)


#DONE
def generate_report(student: Student):
    filename = student_dao.generate_report(student)
    return filename