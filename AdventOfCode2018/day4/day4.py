#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from collections import Counter
from datetime import datetime, timedelta
import re


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()

    line_format_re = re.compile(r'^\[(.*)\] (.*)$')
    wakeup_re = re.compile(r'^wakes up$')
    fall_asleep_re = re.compile(r'^falls asleep$')
    begin_shift_re = re.compile(r'^Guard #(\d+) begins shift$')

    guards_sleep_log = {}   # { guard_id (int) : ( total_time_asleep (int) , minutes_asleep (list(int)) ) }
    sorted_lines = []
    for line in lines:
        timestamp_s, message = line_format_re.match(line).groups()
        timestamp = datetime.strptime(timestamp_s, '%Y-%m-%d %H:%M')
        sorted_lines.append((timestamp, message))

    sorted_lines.sort(key=lambda x: x[0])

    guard_id = -1
    wakeup_time = None
    fall_asleep_time = None
    for line in sorted_lines:
        timestamp, message = line

        match = begin_shift_re.match(message)
        if match:
            # New guard. Initialize variables and dict entry if that guard didn't exist
            wakeup_time = None
            fall_asleep_time = None
            guard_id = int(match.groups()[0])
            if guard_id not in guards_sleep_log:
                guards_sleep_log[guard_id] = [0, []]

            continue

        match = wakeup_re.match(message)
        if match:
            wakeup_time = timestamp
            if fall_asleep_time:
                minutes_asleep = (wakeup_time - fall_asleep_time).total_seconds() / 60.0

                # Add total minutes asleep to guard total
                guards_sleep_log[guard_id][0] += int(minutes_asleep)

                # Add minutes numbers to list of minutes asleep
                time = fall_asleep_time
                while time != wakeup_time:
                    guards_sleep_log[guard_id][1].append(time.minute)
                    time += timedelta(minutes=1)

                wakeup_time = None
                fall_asleep_time = None

            continue

        match = fall_asleep_re.match(message)
        if match:
            if fall_asleep_time is None:
                fall_asleep_time = timestamp


    # Get guard with most time asleep
    max_guard_id = 0
    max_time_asleep = 0
    guards_most_asleep_minutes = {} # { guard_id (int) : ( most rep minute asleep (int) , frequency (int) ) }

    for guard_id, logs in guards_sleep_log.items():
        time_asleep, minutes_asleep = logs
        if time_asleep > max_time_asleep:
            max_time_asleep = time_asleep
            max_guard_id = guard_id

        # Get most repeated minute asleep
        minute_counter = Counter(minutes_asleep)
        if minute_counter:
            guards_most_asleep_minutes[guard_id] = minute_counter.most_common(1)[0]

    # Get most repeated minute asleep
    most_repeated_minute, freq = guards_most_asleep_minutes[max_guard_id]
    product = max_guard_id * most_repeated_minute

    print('PART 1')
    print(f'Guard who slept the most: Guard #{max_guard_id}')
    print(f'Minutes asleep = {max_time_asleep}. Most repeated minute = {most_repeated_minute} ({freq} times)')
    print(f'Product = {max_guard_id} * {most_repeated_minute} = {product}')

    print('\n--------------------------------------\n')
    print('PART 2')

    max_minute_asleep = 0
    max_minute_asleep_freq = 0
    max_guard_id = 0

    for guard_id, logs in guards_most_asleep_minutes.items():
        most_repeated_minute, freq = logs
        if freq > max_minute_asleep_freq:
            max_minute_asleep_freq = freq
            max_minute_asleep = most_repeated_minute
            max_guard_id = guard_id

    product = max_guard_id * max_minute_asleep
    print(f'Guard with the most frequency of repeated minute asleep = Guard #{max_guard_id}')
    print(f'Minute = {max_minute_asleep} ({max_minute_asleep_freq} times)')
    print(f'Product = {max_guard_id} * {max_minute_asleep} = {product}')

 


if __name__ == "__main__":
    main(sys.argv[1])
