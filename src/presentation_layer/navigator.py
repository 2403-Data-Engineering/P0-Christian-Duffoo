from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from menu import Menu

#Navigator file acts as the cursor, 
#changing the current_menu according to the appropiate options

class Navigator:
    def __init__(self):
        from presentation_layer.menu import MainMenu
        from presentation_layer.student_input import StudentInput
        from presentation_layer.professor_input import ProfessorInput
        from presentation_layer.course_input import CourseInput
        self.student_input = StudentInput()
        self.professor_input = ProfessorInput()
        self.course_input = CourseInput()
        self.current_menu = MainMenu(self, self.student_input, self.professor_input, self.course_input)
        self.running = True

    def navigate(self, next_menu: Menu):
        self.current_menu = next_menu

    def quit_program(self):
        print("Terminating program...")
        self.running = False
    

