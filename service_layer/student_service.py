from models.student import Student
from models.course import Course

class StudentService:
    
    def new_student(self, student: Student):
        print("1Temporarily under construction...")
        #User enters information 
        #
    
    def update_student(self, student: Student):
        print("2Temporarily under construction...")
        #User enters student ID
        #Checks if student exists
        #Database returns result and prompts what attribute to change
        #Perform update function

    def remove_student(self, student: Student):
        print("3Temporarily under construction...")
        #User enters student ID
        #Checks if student exists in table
        #Prevent removal if student is enrolled in a course
        #Have to remove enrollment junction from each class
        #Not necessarily drop row, but ignore it to keep data

    def view_students(self, student: Student):
        print("4Temporarily under construction...")
        #Simply queries student table with Select *

    def enroll_student(self, student: Student, course: Course):
        print("6Temporarily under construction...")
        #User enters studentID and courseID
        #First checks if student is already enrolled
        #Adds junction to enrollment table

    def drop_student(self, student: Student, course: Course):
        print("5Temporarily under construction...")
        #User enters studentID and courseID
        #First checks if student exists in course
        #Ignores row instead of deleting row?

    def generate_report(self, student: Student):
        print("7Temporarily under construction...")
        #Find all classes of a student with studentID in enrollment table
        #