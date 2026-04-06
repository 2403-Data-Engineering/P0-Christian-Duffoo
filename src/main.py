import presentation_layer.navigator as navigator


if __name__ == "__main__":

    while navigator.running == True:
        navigator.current_menu.render()
    print("Program terminated. Have a great day!")
    
    