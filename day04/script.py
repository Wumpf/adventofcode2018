#!/usr/bin/python3
import re

# test input
# data = [
#     '[1518-11-01 00:00] Guard #10 begins shift',
#     '[1518-11-01 00:05] falls asleep',
#     '[1518-11-01 00:25] wakes up',
#     '[1518-11-01 23:58] Guard #99 begins shift',
#     '[1518-11-03 00:24] falls asleep',
#     '[1518-11-02 00:40] falls asleep',
#     '[1518-11-02 00:50] wakes up',
#     '[1518-11-01 00:55] wakes up',
#     '[1518-11-03 00:05] Guard #10 begins shift',
#     '[1518-11-01 00:30] falls asleep',
#     '[1518-11-03 00:29] wakes up',
#     '[1518-11-04 00:36] falls asleep',
#     '[1518-11-05 00:03] Guard #99 begins shift',
#     '[1518-11-04 00:46] wakes up',
#     '[1518-11-04 00:02] Guard #99 begins shift',
#     '[1518-11-05 00:45] falls asleep',
#     '[1518-11-05 00:55] wakes up',
# ]

# file input
data = open('input.txt').readlines()

# ----------------------------------------------------------------

time_regex = re.compile('\[1518-(?P<m>\d+)-(?P<d>\d+) (?P<h>\d+):(?P<min>\d+)\]')
def get_absolute_minutes(event):
    time = time_regex.match(event)
    return int(time.group('m')) * 31 * 24 * 60 + int(time.group('d')) * 24 * 60 + int(time.group('h')) * 60 + int(time.group('min'))

data.sort(key=get_absolute_minutes)

guard_shift_regex = re.compile('\[\d+-\d+-\d+ \d+:\d+\] Guard #(?P<id>\d+) begins shift')
guards = {}
cur_guard = None
cur_sleep_start = 0
for event in data:
    if 'begins shift' in event:
        cur_guard = guard_shift_regex.match(event).group('id')
    elif 'falls asleep' in event:
        cur_sleep_start = int(time_regex.match(event).group('min'))
    elif 'wakes up' in event:
        sleep_range = (cur_sleep_start, int(time_regex.match(event).group('min')))
        if cur_guard in guards:
            guards[cur_guard].append(sleep_range)
        else:
            guards[cur_guard] = [ sleep_range ]


sleepiest_guard = max(zip(guards.keys(), guards.values()), key = lambda guard: sum(sleeprange[1] - sleeprange[0] for sleeprange in guard[1]))

minutes = [0] * 60
for sleep_range in sleepiest_guard[1]:
    for i in range(sleep_range[0], sleep_range[1]):
        minutes[i] += 1
sleepiest_minute = minutes.index(max(minutes))

print('result part one:', int(sleepiest_guard[0]) * sleepiest_minute)

# ----------------------------------------------------------------


print('result part two:', 0)