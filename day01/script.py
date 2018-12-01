#!/usr/bin/python3

# test input
#data = '+1, +1, +1'
#data = '+1, +1, -2'
#data = '-1, -2, -3'
# file input
data = open('input.txt').read()

executable = data.replace(",", "").replace("\n", "")
result = eval(executable)
print('result part one:', result)

# ----------------------------------------------------------------

ops = data.split("\n")
frequency = 0
known_frequencies = set()

class Found(Exception): pass
try:
    while True:
        for op in ops:
            frequency += int(op)
            if frequency in known_frequencies:
                raise Found
            known_frequencies.add(frequency)
except Found:
    print('result part two:', frequency)
