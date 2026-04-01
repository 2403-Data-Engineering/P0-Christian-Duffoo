current_state = None
running = True
def navigate(next_state):
    global current_state
    current_state = next_state

class Name:

    
    def __init__(self):
        pass

    def render(self):
        pass

class Menu(Name):
    name = "Menus"
    def render(self):
        global current_state
        global running
        print("""
===============
1) Foo machine
2) Bar machine
0) Quit program
              """)
        
        user_input = input()

        match user_input:
            case "1": 
                print("Entering the foo machine...")
                current_state = Bofa()
            case "2":
                print("currently invalid, choose something else")
            case "0":
                print("quitting program...")
                running = False
            
                
class Bofa(Name):
    name = "bofas"
    def render(self):
        global current_state
        print("""
==========
1) Print "bofa"
2) exit             
              """)
        user_input = input()
        match user_input:
            case "1":
                print("Foo fighters when they see a foo")
                current_state = Menu()
            case "2":
                print("returning to main menu...")
                navigate(Menu())


if __name__ == "__main__":
    current_state = Menu()
    while(running):
        current_state.render()
        