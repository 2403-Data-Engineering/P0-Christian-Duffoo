from models.student import Student
from models.course import Course

student_john = Student("20", "John", "Smith", "smith@john.com", "CS", "Freshman")
student_jane = Student("21", "Jane", " Doe", "jane.doe@school.edu", "Math", "Junior")
student_chris = Student("22", "Chris", "Duffoo", "chris.duffoo@college.net", "ECE", "Senior")

student_list = [student_john, student_jane, student_chris]


def save_new_student(new_student: Student):

    print(new_student)
    print(f"Saved student {new_student.first_name} {new_student.last_name} into the system!")
        #This is a placeholder, will actually interact with database 
        #Ensure email is unique?
        #If new student is valid, enter it into sql student table
        #If invalid, return invalid message and do not insert
        #Put constraints on the sql table

    
def update_student(selected_student: Student, user_int: str, user_input: str):
    #TODO: Updates selected_student (already confirmed to exist) attribute according to int
    #Database returns result and prompts what attribute to change
    #Perform update function
    attribute = ""
    match user_int:
        case "1":
            attribute = "First Name"
        case "2":
            attribute = "Last Name"
        case "3":
            attribute = "Email"
        case "4":
            attribute = "Major"
        case "5":
            attribute = "Year"

    print(f"Student {selected_student.first_name} {selected_student.last_name}'s attribute: {attribute} has been updated to {user_input}")
    #TODO: Update to interact with the database

def remove_student(selected_student: Student):
    #TODO: Call database to remove row with student 
    print(f"Removed student: {selected_student.first_name} {selected_student.last_name} from the system.")
        
        #User enters student ID
        #Checks if student exists in table
        #Prevent removal if student is enrolled in a course
        #Have to remove enrollment junction from each class
        #Not necessarily drop row, but ignore it to keep data

def view_students():
    #TODO: SELECT * from student table
    print(*student_list, sep='\n')


def enroll_student(student: Student, course: Course):
    #TODO: Insert into enrollment table
    print(f"Enrolled student {student.first_name} {student.last_name} into {course.course_name}.")
    #First checks if student is already enrolled
    #Adds junction to enrollment table

def drop_student(student: Student, course: Course):
    #TODO: Drop row from enrollment table
    print(f"Dropped student {student.first_name} {student.last_name} from {course.course_name}")
    #First checks if student exists in course
    #Ignores row instead of deleting row?

def generate_report(student: Student):
    #TODO: Queries enrollment table and converts it to HTML
    #Find all classes of a student with studentID in enrollment table
    return "user/p0/output/report.html"
    #maybe returns filepath of html file?

def get_student_from_id(id: str):
    student_josh = Student("20", "Josh", "Smith", "smith@josh.com", "CS", "Freshman")
    #^Place holder: Change to query the student database to find student with parameter ID
    return student_josh
    #Maybe change to terminate program if invalid id:

def check_enrollment(selected_student: Student):
    #TODO: Check if student is enrolled in one or more courses, return True if they have any enrollments
    return False

def view_enrollment(student: Student):

    enrollment_list = ["404 Python", "123 SQL"]
    #TODO: Check number of rows student has in enrollment table
    print(f"{student.first_name} {student.last_name}'s enrolled courses:")
    for enrollment in enrollment_list:
        print(enrollment)
