from data_layer.db_connection_manager import get_connection
from yattag import Doc, indent
from mdutils.mdutils import MdUtils



def save_student(student):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = """INSERT INTO student (first_name, last_name, email, major, school_year)
                 VALUES (%s, %s, %s, %s, %s)"""
        values = [student.first_name, student.last_name, student.email, student.major, student.school_year]
        cursor.execute(sql, values)


def view_all_students():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM student")
        return cursor.fetchall()
    

def update_student(student_id: int, attribute: str, user_input: str):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = f"""  UPDATE student
                    SET {attribute} = %s
                    WHERE student_id = %s"""
        values = [user_input, student_id]
        cursor.execute(sql, values)


def drop_student(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "DELETE FROM student WHERE student_id = %s"
        cursor.execute(sql, [id])


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


def view_enrollment(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)

        sql = """SELECT course_id, course_name
                 FROM student NATURAL JOIN enrollment NATURAL JOIN course
                 WHERE student_id = %s"""
        cursor.execute(sql, [id])
    
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
    

def generate_report(student):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = """SELECT course_id, course_name
                 FROM student NATURAL JOIN enrollment NATURAL JOIN course
                 WHERE student_id = %s
                 LIMIT 20"""
        cursor.execute(sql, [student.student_id])
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

    md = MdUtils(file_name="student_report", title="Student Enrollment Report")

    md.new_header(level=1, title=f"{student.first_name} {student.last_name} (ID: {student.student_id})")


    table_data = list(columns)
    for row in rows:
        for cell in row.values():
            table_data.append(str(cell))

    md.new_table(
        columns=len(columns),
        rows=len(rows) + 1,
        text=table_data,
        text_align="center")

    md.create_md_file()
    
    return "student_report.md"