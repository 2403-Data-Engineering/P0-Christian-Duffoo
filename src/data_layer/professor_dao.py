from data_layer.db_connection_manager import get_connection
from mdutils.mdutils import MdUtils



def save_professor(professor):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = """INSERT INTO professor (first_name, last_name, department, email)
                 VALUES (%s, %s, %s, %s)"""
        values = [professor.first_name, professor.last_name, professor.department, professor. email]
        cursor.execute(sql, values)


def view_all_professors():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM professor")
        return cursor.fetchall()
    

def update_professor(professor_id: int, attribute: str, user_input: str):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = f"""  UPDATE professor
                    SET {attribute} = %s
                    WHERE professor_id = %s"""
        values = [user_input, professor_id]
        cursor.execute(sql, values)


def drop_professor(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "DELETE FROM professor WHERE professor_id = %s"
        cursor.execute(sql, [id])


def get_professor_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM professor WHERE professor_id = %s", [id])
        return cursor.fetchone()
    

def count_rows(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = "SELECT COUNT(*) FROM course WHERE prof_id = %s"

        cursor.execute(sql, [id])
        return cursor.fetchone()
    

def generate_report(professor):
    rows = None
    columns = None
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        sql = """   SELECT c.course_id, c.course_name, s.student_id, s.first_name, s.last_name
                    FROM professor as p
                    INNER JOIN course AS c ON p.professor_id = c.prof_id
                    INNER JOIN enrollment AS e ON c.course_id = e.course_id
                    INNER JOIN student AS s ON e.student_id = s.student_id
                    WHERE p.professor_id = %s
                    ORDER BY c.course_id, s.student_id
                    LIMIT 100"""
        cursor.execute(sql, [professor.professor_id])
        rows = cursor.fetchall()
        columns = [desc[0] for desc in cursor.description]

    md = MdUtils(file_name="professor_report", title="Professor Report")
    name = f"{professor.first_name} {professor.last_name}"

    md.new_header(level=1, title=f"Here are the courses instructed by {name} and their enrolled students:")


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
    
    return "professor_report.md"