from playsound import playsound
import time
def main():
    testing = True
    alarm=input("What time would you like the alarm to play. Put in H:M:S")
    while testing ==True:
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        if current_time >= alarm:
            playsound("alarm.wav")
            testing=False
        else:
            pass
        #print(current_time)

main()
