#!/usr/bin/python3

# test input
#pathregex = '^ENWWW(NEEE|SSE(EE|N))$'
#pathregex = '^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$'
#pathregex = '^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$'
#pathregex = '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'

# puzzle input
pathregex = open('day20/input.txt').read()

# ----------------------------------------------------------------

nodes = { (0,0):set() }

d = {'N': (-1, 0), 'S': (1, 0), 'W': (0, 1), 'E': (0, -1)}

def find_longest(path, i, positions):
    positions_before = positions.copy()
    subexpr_outcomes = set()
    while i < len(path):
        if path[i] == '|':
            subexpr_outcomes = subexpr_outcomes.union(positions)
            positions = positions_before.copy()
        elif path[i] == '(':
            i, positions = find_longest(path, i + 1, positions)
        elif path[i] == ')':
            subexpr_outcomes = subexpr_outcomes.union(positions)
            return (i, subexpr_outcomes)
        else:
            positions_new = set()
            for pos in positions:
                pos_new = (pos[0] + d[path[i]][0], pos[1] + d[path[i]][1])
                positions_new.add(pos_new)
                if pos_new not in nodes:
                    nodes[pos_new] = set()
                try:
                    nodes[pos].add(pos_new)
                except:
                    pass
            positions = positions_new
        i += 1

find_longest(pathregex[1:-1], 0, { (0,0) })

#def breadth_first():
visited_nodes = set()
visiting_queue = [(0,0)]
gen = -1
while len(visiting_queue) > 0:
    visited_nodes = visited_nodes.union(visiting_queue)
    visiting_queue = [child for n in visiting_queue if n in nodes for child in nodes[n] if child not in visited_nodes]
    gen += 1
    if gen == 999:
        print('result part two:', len(nodes) - len(visited_nodes))

print('result part one:', gen)
