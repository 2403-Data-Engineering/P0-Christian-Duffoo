from data_layer.db_connection_manager import get_connection

def view_all_students():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student")
        return cursor.fetchall()
    

def get_student_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student WHERE student_id = %s", [id])
        return cursor.fetchone()
    
    
def count_rows(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT COUNT(*) FROM enrollment WHERE student_id = %s"

        cursor.execute(sql, [id])
        return cursor.fetchone()
    

def drop_student(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "DELETE FROM student WHERE student_id = %s"

        cursor.execute(sql, [id])


def save_student(student):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = """INSERT INTO student (first_name, last_name, email, major, school_year)
                 VALUES (%s, %s, %s, %s, %s)"""
        values = [student.first_name, student.last_name, student.email, student.major, student.school_year]
        cursor.execute(sql, values)


def view_enrollment(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        sql = """SELECT course_id, course_name
                 FROM student NATURAL JOIN enrollment NATURAL JOIN course
                 WHERE student_id = %s"""
        cursor.execute(sql, [id])
    
        return cursor.fetchall()
    

def enroll_student_in_course(student_id: int, course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "INSERT INTO enrollment(student_id, course_id) VALUES(%s, %s)"
        values = [student_id, course_id]
        cursor.execute(sql, values)


def drop_student_from_course(student_id: int, course_id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "DELETE FROM enrollment WHERE student_id = %s AND course_id = %s"
        values = [student_id, course_id]
        cursor.execute(sql, values)



    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)


    