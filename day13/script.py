#!/usr/bin/python3

# test input
data_raw = [
    '/->-\\        ',
    '|   |  /----\\',
    '| /-+--+-\\  |',
    '| | |  | v  |',
    '\\-+-/  \\-+--/',
    '  \\------/   ',
]

# puzzle input    
data_raw = open('day13/input.txt').readlines()

# ----------------------------------------------------------------

from itertools import count

directions = ((1,0), (0, 1), (-1, 0), (0, -1))

carts = []
tracks = []
for y, row in enumerate(data_raw):
    for x, letter in enumerate(row):
        cart = { 'x': x, 'y': y, 'd': 0, 'mem': -1 }
        if letter == '>':
            cart['d'] = 0
            carts.append(cart)
        elif letter == 'v':
            cart['d'] = 1
            carts.append(cart)
        elif letter == '<':
            cart['d'] = 2
            carts.append(cart)
        elif letter == '^':
            cart['d'] = 3
            carts.append(cart)
    tracks.append(row.replace('>', '-').replace('<', '-').replace('v', '|').replace('^', '|'))

print('num carts', len(carts))

collision = None
for _ in count():
    carts.sort(key=lambda cart: cart['x'])
    carts.sort(key=lambda cart: cart['y'])
    for cart in carts:
        d = cart['d']
        if d == None:
            continue
        cur_track = tracks[cart['y']][cart['x']]
        assert(cur_track != ' ')
        if cur_track == '\\':
            if d == 0:
                d = 1
            elif d == 1:
                d = 0
            elif d == 2:
                d = 3
            elif d == 3:
                d = 2
        elif cur_track == '/':
            if d == 0:
                d = 3
            elif d == 1:
                d = 2
            elif d == 2:
                d = 1
            elif d == 3:
                d = 0
        elif cur_track == '+':
            d = (d + cart['mem']) % 4
            cart['mem'] += 1
            if cart['mem'] > 1:
                cart['mem'] = -1

        cart['d'] = d
        cart['x'] += directions[d][0]
        cart['y'] += directions[d][1]

        # detect collisions
        for cart2 in carts:
            if cart2 != cart and cart2['d'] != None and cart['x'] == cart2['x'] and cart['y'] == cart2['y']:
                print('collision:', cart['x'], cart['y'])
                cart2['d'] = None
                cart['d'] = None
                break

    # clean deleted carts
    carts = [cart for cart in carts if cart['d'] != None]
    if len(carts) == 1:
        print('last cart is at:', carts[0]['x'], carts[0]['y'])
        break