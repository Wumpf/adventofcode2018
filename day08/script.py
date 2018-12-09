#!/usr/bin/python3

# test input
data_raw = '2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'

# file input    
data_raw = open('day08/input.txt').read()

# ----------------------------------------------------------------

from collections import namedtuple

Node = namedtuple('Node', ['meta', 'children'])
nodes = []

data = [int(d) for d in data_raw.split(' ')]

def build_tree(data_slice):
    if not data_slice:
        return None
    num_children = data_slice[0]
    num_meta = data_slice[1]
    data_slice = data_slice[2:]

    children = []
    for _ in range(num_children):
        data_slice, child = build_tree(data_slice)
        children.append(child)
    
    node = Node(meta=data_slice[0:num_meta], children=children)
    return data_slice[num_meta:], node

_, root_node = build_tree(data)

# ----------------------------------------------------------------

def count_meta(node):
    return sum(node.meta) + sum(count_meta(child) for child in node.children)

print('result part one:', count_meta(root_node))

# ----------------------------------------------------------------

def count_special(node):
    if not node.children:
        return sum(node.meta)
    return sum(count_special(node.children[meta - 1]) for meta in node.meta if meta != 0 and meta <= len(node.children))

print('result part two:', count_special(root_node))