from pynput.mouse import Button, Controller
import keyboard
import time
from typing import password
mouse=Controller()
def main():
    while True:
        if keyboard.is_pressed("`") == True:
            macro()
            quit()
        else:
            pass
def click():
    mouse.press(Button.left)
    mouse.release(Button.left)
def macro():
    position = mouse.position
    mouse.position = (486,477)
    click()
    time.sleep(3)
    mouse.position = (857,535)
    click()
    time.sleep(12)
    password()
    mouse.position = (756,508)
    click()
    time.sleep(2)
    mouse.position = (612, 813)
    time.sleep(3)
    click()
    time.sleep(3)
    mouse.position = (598,478)
    click()
    time.sleep(3)
    mouse.position = (784,422)
    click()
    mouse.position=position
main()
