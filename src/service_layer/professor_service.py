from models.student import Student
from models.professor import Professor
from models.course import Course

professor_smark = Professor("12", "Mark", "Smark", "Science", "mark.smark@emark.com")
professor_fisher = Professor("13", "Ashley", "Fisher", "Psychology", "ashley.fisher@school.edu")
professor_johnson = Professor("9", "Dwayne", "Johnson", "Electrical", "dwayne.johnson@wrestle.mania")

professor_list = [professor_smark, professor_fisher, professor_johnson]


def save_new_professor(professor: Professor):
    print(professor)
    print(f"Saved professor {professor.first_name} {professor.last_name} into the system!")
        #This is a placeholder, will actually interact with database 
        #Ensure email is unique?
        #If new student is valid, enter it into sql student table
        #If invalid, return invalid message and do not insert
        #Put constraints on the sql table


def view_professors():
    #TODO: SELECT * from student table
    print(*professor_list, sep='\n')


def get_professor_from_id(id: str):
    #^Place holder: Change to query the student database to find student with parameter ID
    return professor_johnson
    #Maybe change to terminate program if invalid id:


def update_professor(selected_professor: Professor, user_int: str, user_input: str):
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
            attribute = "Department"
        case "4":
            attribute = "Email"

    print(f"Professor {selected_professor.first_name} {selected_professor.last_name}'s attribute: {attribute} has been updated to {user_input}")
    #TODO: Update to interact with the database

def remove_professor(selected_professor: Professor):
    #TODO: Call database to remove row with student 
    print(f"Removed professor: {selected_professor.first_name} {selected_professor.last_name} from the system.")
        
        #User enters student ID
        #Checks if student exists in table
        #Prevent removal if student is enrolled in a course
        #Have to remove enrollment junction from each class
        #Not necessarily drop row, but ignore it to keep data


def check_instructed_courses(profesor: Professor):
    #TODO: Check if student is enrolled in one or more courses, return True if they have any enrollments
    return False

def generate_report(professor: Professor):
    #TODO: Queries enrollment table and converts it to HTML
    #Find all classes of a student with studentID in enrollment table
    return "user/p0/output/report.html"
    #maybe returns filepath of html file?
