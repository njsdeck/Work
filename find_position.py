from pynput.mouse import Button, Controller
import keyboard
mouse=Controller()
while True:
    if keyboard.is_pressed("`") == True:
        position = mouse.position
        print(position)
        quit()
    else:
        pass
