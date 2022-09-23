from playsound import playsound
import time
import keyboard
def main():
    type = input("1 for add time, 2 for specify time.")
    if type == '1':
        addition()
    if type == '2':
        noise()
def noise():
    alarm = input("What time would you like the alarm to play? Put in H:M:S. If the hour is not passed 10 am then you must put a 0 in front. For example, if it was 8am then the hour section would be 08 not 8")
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Alarm set")
    while current_time != alarm:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if keyboard.is_pressed("`") == True:
            quit()
    playsound("alarm.wav")
def addition():
    new = int(input("How many minutes would you like to add"))
    t0 = time.time()
    t1 = t0 + (60*new)
    alarm_time = time.strftime("%I %M %p",time.localtime(t1))
    t = time.time()
    current_time = time.strftime("%I %M %p", time.localtime(t))
    print("Alarm Set")
    while current_time != alarm_time:
        t = time.time()
        current_time = time.strftime("%I %M %p", time.localtime(t))
        if keyboard.is_pressed("`") == True:
            quit()
    playsound("alarm.wav")
main()
