#! python3
# countdown.py - A simple countdown script

import time
import subprocess

time_left = 60
while time_left > 0:
    print(time_left)
    time.sleep(1)
    time_left -= 1

# at end of countdown, play a sound file
subprocess.Popen(['alarm.wav'], shell=True)