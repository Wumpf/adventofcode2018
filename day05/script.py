#!/usr/bin/python3

# test input
#data = 'dabAcCaCBAcCcaDA'

# file input
data = open('input.txt').read()

# ----------------------------------------------------------------

polymer = list(data)
oldlen = 0
while oldlen != len(polymer):
    oldlen = len(polymer)
    for pidx, letter in enumerate(polymer[1:]):
        if letter != polymer[pidx] and letter.lower() == polymer[pidx].lower():
            # too slow
            #polymer = polymer[:pidx] + polymer[pidx+2:]
            # too slow
            #polymer.pop(pidx)
            #polymer.pop(pidx)
            # too slow?
            del polymer[pidx]
            del polymer[pidx]
            break

print('result part one:', len(polymer))

# ----------------------------------------------------------------
