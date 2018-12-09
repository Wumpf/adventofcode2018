#!/usr/bin/python3

# test input
#num_players, last_marble = 9, 25
#num_players, last_marble = 10, 1618
#num_players, last_marble = 13, 7999
#num_players, last_marble = 17, 1104
#num_players, last_marble = 21, 6111
#num_players, last_marble = 30, 5807

# file input    
num_players, last_marble = 405, 70953

# ----------------------------------------------------------------

# normal list is unusable here
from blist import blist

def solve(num_players, last_marble):
    cur_idx = 0
    cur_player = 0
    scores = [0] * num_players
    circle = blist([0])

    marble = 1
    while marble <= last_marble:
        for _ in range(23 - marble % 23):
            cur_idx = (cur_idx + 1) % len(circle) + 1
            circle.insert(cur_idx, marble)
            marble += 1

        # scoring
        cur_idx = (cur_idx - 6) % (len(circle)) - 1
        scores[marble % num_players] += marble + circle[cur_idx]
        
        # avoid doing a pop by doing the next insert here as well.
        cur_idx_nxt = (cur_idx + 1) % len(circle)
        circle[cur_idx] = circle[cur_idx_nxt]
        cur_idx = (cur_idx + 2) % len(circle)
        circle[cur_idx_nxt] = circle[cur_idx]
        circle[cur_idx] = marble + 1
        marble += 2

    return max(scores)

print('result part one:', solve(num_players, last_marble))
print('result part two:', solve(num_players, last_marble * 100))

