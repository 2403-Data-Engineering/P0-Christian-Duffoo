from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from menu import Menu

#Navigator file acts as the cursor, 
#changing the current_menu according to the appropiate options

class Navigator:
    def __init__(self):
        from presentation_layer.menu import MainMenu
        from presentation_layer.input_text import InputText
        self.input_text = InputText()
        self.current_menu = MainMenu(self, self.input_text)
        self.running = True

    def navigate(self, next_menu: Menu):
        self.current_menu = next_menu

    def quit_program(self):
        print("Terminating program...")
        self.running = False
    

