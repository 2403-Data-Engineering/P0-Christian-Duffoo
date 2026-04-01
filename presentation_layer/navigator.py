from __future__ import annotations
from typing import TYPE_CHECKING

from service_layer.student_service import StudentService

if TYPE_CHECKING:
    from presentation_layer.menu import Menu

#Navigator file acts as the cursor, 
#hanging the current_menu according to the appropiate options

class Navigator:
    def __init__(self, student_service: StudentService):
        from presentation_layer.menu import MainMenu
        self.current_menu = MainMenu(self)
        self.running = True
        self.student_service = student_service

    def navigate(self, next_menu: Menu):
        self.current_menu = next_menu

    def quit_program(self):
        print("Terminating program...")
        self.running = False
    

