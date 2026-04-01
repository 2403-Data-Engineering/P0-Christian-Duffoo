from presentation_layer.navigator import Navigator
from service_layer.student_service import StudentService


if __name__ == "__main__":
    
    terminal = Navigator(StudentService())
    while(terminal.running):
        terminal.current_menu.render()
    print("Program terminated. Have a great day!")