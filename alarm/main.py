import time
import datetime
import pygame

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "/home/kennedy/vscode/github/Music/nakam_sai_lil_maina_x_sosatheprodigy_mp3_21583.mp3"

if __name__ == "__main__":
    alarm_time = input("Enter the alrm time (HH:MM:SS): ")
    set_alarm(alarm_time)