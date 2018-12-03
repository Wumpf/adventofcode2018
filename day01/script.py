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

from itertools import count, islice, cycle, takewhile

#all_sums_generator = (sum(int(open('input.txt').readlines()[i % len(open('input.txt').readlines())]) for i in range(x)) for x in count())

all_sums_generator = (sum(int(op) for op in islice(cycle(open('input.txt').readlines()), x)) for x in count())

#[print(i) for i in islice(all_sums_generator, 10)]

[print(i) for i in count() if len(set(islice(all_sums_generator, i))) != i]

# [ print(p) for p in ((open('input.txt').readlines()[x % len(open('input.txt').readlines()) for x in count()) )]