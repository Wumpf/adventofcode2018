#!/usr/bin/python3

# test input
#data = ['abcdef', 'bababc', 'abbcde', 'abcccd', 'aabcdd', 'abcdee', 'ababab']
# data = [
#     'abcde',
#     'fghij',
#     'klmno',
#     'pqrst',
#     'fguij',
#     'axcye',
#     'wvxyz',
# ]

# file input
data = open('input.txt').readlines()

# ----------------------------------------------------------------

l2 = len([bid for bid in data if any(bid.count(chr(letter)) == 2 for letter in range(ord('a'), ord('z')+1))])
l3 = len([bid for bid in data if any(bid.count(chr(letter)) == 3 for letter in range(ord('a'), ord('z')+1))])
print('result part one:', l2 * l3)

# silly oneliner
#print('result part one:', len([bid for bid in open('input.txt').readlines() if any(bid.count(chr(letter)) == 2 for letter in range(ord('a'), ord('z')+1))]) * len([bid for bid in open('input.txt').readlines() if any(bid.count(chr(letter)) == 3 for letter in range(ord('a'), ord('z')+1))]))

# ----------------------------------------------------------------

for idx, bid1 in enumerate(data[:-1]):
    for bid2 in data[(idx+1):]:
        overlap = ''.join(letter1 for letter1, letter2 in zip(list(bid1), list(bid2)) if letter1 == letter2)
        if len(overlap) == len(bid1) -1:
            print('result part two:', overlap)

# incredibly silly one-liner:
#[print('result part two:', overlap) for overlap in (''.join(letter1 for letter1, letter2 in zip(list(bid1), list(bid2)) if letter1 == letter2) for idx, bid1 in enumerate(data[:-1]) for bid2 in data[(idx+1):]) if (len(overlap) == len(data[0]) -1)]

