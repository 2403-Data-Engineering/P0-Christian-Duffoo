from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from menu import Menu

#Navigator file acts as the cursor,
#changing the current_menu according to the appropiate options
from presentation_layer.menu import MainMenu
from presentation_layer.student_input import StudentInput
from presentation_layer.professor_input import ProfessorInput
from presentation_layer.course_input import CourseInput

student_input = StudentInput()
professor_input = ProfessorInput()
course_input = CourseInput()
current_menu = MainMenu(student_input, professor_input, course_input)
running = True

def navigate(next_menu: Menu):
    global current_menu
    current_menu = next_menu

def quit_program(self):
    global running
    print("Terminating program...")
    running = False