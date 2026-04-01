from presentation_layer.navigator import Navigator


if __name__ == "__main__":
    
    terminal = Navigator()
    while(terminal.running):
        terminal.current_menu.render()
    print("Program terminated. Have a great day!")