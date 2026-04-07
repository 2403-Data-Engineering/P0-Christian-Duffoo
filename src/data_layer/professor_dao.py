from data_layer.db_connection_manager import get_connection
from yattag import Doc, indent



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

    doc, tag, text, line = Doc().ttl()
    professor_name = f"{professor.first_name} {professor.last_name}"

    doc.asis('<!DOCTYPE html>')
    with tag('html', lang='en'):
        with tag('head'):
            doc.stag('meta', charset='utf-8')
            line('title', 'MySQL Query Report')
            with tag('style'):
                text("table { border-collapse: collapse; width: 100%; }")
                text("th, td { border: 1px solid black; padding: 8px; text-align: left; }")
        with tag('body'):
            line('h1', f"{professor_name}'s (ID: {professor.professor_id}) instructed courses and their students:")
            with tag('p', klass='meta'):
                text(f"Total records: {len(rows)}")

            with tag('table'):
                # Header row
                with tag('thead'):
                    with tag('tr'):
                        for col in columns:
                            line('th', col.replace('_', ' ').title())
                # Data rows
                with tag('tbody'):
                    for row in rows:
                        with tag('tr'):
                            for col in columns:
                                line('td', str(row[col]) if row[col] is not None else '—')

    html_output = indent(doc.getvalue())
    with open('professor_report.html', 'w') as f:
        f.write(html_output)

    return "professor_report.html"