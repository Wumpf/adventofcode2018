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

l2 = sum(any(bid.count(letter) == 2 for letter in list(bid)) for bid in data)
l3 = sum(any(bid.count(letter) == 3 for letter in list(bid)) for bid in data)
print('result part one:', l2 * l3)

# silly oneliner
#print('result part one:', sum(any(bid.count(letter) == 2 for letter in list(bid)) for bid in data) * sum(any(bid.count(letter) == 3 for letter in list(bid)) for bid in data))

# ----------------------------------------------------------------

for idx, bid1 in enumerate(data[:-1]):
    for bid2 in data[(idx+1):]:
        overlap = ''.join(letter1 for letter1, letter2 in zip(list(bid1), list(bid2)) if letter1 == letter2)
        if len(overlap) == len(bid1) -1:
            print('result part two:', overlap)

# incredibly silly one-liner:
#[print('result part two:', overlap) for overlap in (''.join(letter1 for letter1, letter2 in zip(list(bid1), list(bid2)) if letter1 == letter2) for idx, bid1 in enumerate(data[:-1]) for bid2 in data[(idx+1):]) if (len(overlap) == len(data[0]) -1)]

