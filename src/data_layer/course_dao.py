from data_layer.db_connection_manager import get_connection

def get_course_by_id(id: int):
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM course WHERE course_id = %s", [id])
        return cursor.fetchone()
    
def view_all_courses():
    with get_connection() as conn:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM course")
        return cursor.fetchall()