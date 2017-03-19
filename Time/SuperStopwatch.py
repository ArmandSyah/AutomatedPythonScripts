#! python3
# stopwatch.py - A simple stopwatch program.

import time

# Display the program's instructions
print('Press ENTER to begin. Afterwards, press ENTER to "click" the stopwatch. Press Ctrl-C to quit.')
input()
print('Started')
start_time = time.time()
last_time = start_time
lap_number = 1

# Start tracking the lap times
try:
    while True:
        input()
        lap_time = round(time.time() - last_time, 2)
        total_time = round(time.time() - start_time, 2)
        print('Lap #{}: {} {}'.format(lap_number, total_time, lap_time), end='')
        lap_number += 1
        last_time = time.time() # reset the last lap time
except KeyboardInterrupt:
    print('\nDone')