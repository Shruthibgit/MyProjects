#Program to Build an alarm clock with snooze option. 
# Please delete this line

import time
from pygame import mixer

#Function to Play the music
def play_music():
    mixer.init()
    mixer.music.load("flute.wav")
    mixer.music.play()

#Function to stop the music
def stop_music():
    mixer.music.stop()

# Function to set the alarm time
def set_alarm():
    while True:
        current_time = time.strftime("%H:%M")
        if current_time == alarm_time:
            print("Time to wake up!!!")
            play_music()
            break
        time.sleep(1)


# Function to snooze the alarm time
def snooze_alarm():
    while True:

        snooze = input("Press enter to snooze for {} minutes, or q to quit: ".format(snooze_time))
        if snooze.lower() == "q":
            break        
        print("Snoozing the alarm")
        stop_music()
        time.sleep(snooze_time * 60)
        play_music()
        print("WAKE UP!!!!")




alarm_time = input("Enter the time to set the alarm (HH:MM): ")
snooze_time = 1
set_alarm()
snooze_alarm()