from models.student import Student
from models.course import Course


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

def remove_student():
        print("3Temporarily under construction...")
        #User enters student ID
        #Checks if student exists in table
        #Prevent removal if student is enrolled in a course
        #Have to remove enrollment junction from each class
        #Not necessarily drop row, but ignore it to keep data

def view_students():
    print("4Temporarily under construction...")
    #Simply queries student table with Select *

def enroll_student():
    print("5Temporarily under construction...")
    #User enters studentID and courseID
    #First checks if student is already enrolled
    #Adds junction to enrollment table

def drop_student():
    print("6Temporarily under construction...")
    #User enters studentID and courseID
    #First checks if student exists in course
    #Ignores row instead of deleting row?

def generate_report():
    print("7Temporarily under construction...")
    #Find all classes of a student with studentID in enrollment table
    #

def get_student_from_id(id: str):
    student_type = Student("20", "John", "Smith", "smith@john.com", "CS", "Freshman")
    #^Place holder: Change to query the student database to find student with parameter ID
    return student_type