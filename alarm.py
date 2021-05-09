from playsound import playsound
import time
import keyboard
def main():
    alarm=input("What time would you like the alarm to play. Put in H:M:S")
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    while current_time != alarm:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if keyboard.is_pressed("`") == True:
            quit()
        else:
            pass
    playsound("alarm.wav")
main()
