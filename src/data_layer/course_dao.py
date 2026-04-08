from data_layer.db_connection_manager import get_connection



def save_course(course):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "INSERT INTO course(course_name, prof_id) VALUES (%s, %s)"
        values = [course.course_name, course.prof_id]
        cursor.execute(sql, values)

        sql = "SELECT first_name, last_name FROM professor WHERE professor_id = %s"
        values = [course.prof_id]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        result = f"{result["first_name"]}" + f" {result["last_name"]}"

        return result


def view_all_courses():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM course")
        return cursor.fetchall()


def edit_course(course_id: int, attribute: str, user_input: str):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = f"""  UPDATE course
                    SET {attribute} = %s
                    WHERE course_id = %s"""
        values = [user_input, course_id]
        cursor.execute(sql, values)


def drop_course(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "DELETE FROM course WHERE course_id = %s"
        cursor.execute(sql, [id])


def view_enrollment(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = """   SELECT s.student_id, s.first_name, s.last_name
                    FROM course AS c NATURAL JOIN enrollment as e NATURAL JOIN student as s
                    WHERE c.course_id = %s """
        value = [id]
        cursor.execute(sql, value)
        result = cursor.fetchall()
        return result




def get_course_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM course WHERE course_id = %s", [id])
        return cursor.fetchone()
    