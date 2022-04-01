from playsound import playsound
import time
import keyboard
def main():
    alarm=input("What time would you like the alarm to play. Put in H:M:S. If the hour is not passed 10 am then you must put a 0 in front. For example, if it was 8am then the hour section would be 08 not 8")
    noise(alarm)
def noise(alarm):
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("alarm set")
    while current_time != alarm:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if keyboard.is_pressed("`") == True:
            quit()
    playsound("alarm.wav")
main()
