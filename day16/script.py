#!/usr/bin/python3

# test input
# data_raw = [
#     'Before: [3, 2, 1, 1]',
#     '9 2 1 2',
#     'After:  [3, 2, 2, 1]',
#     ' '
# ]

# puzzle input
data_raw = [line.strip() for line in open('day16/input.txt').readlines()]
program = [line.strip() for line in open('day16/program.txt').readlines()]

# ----------------------------------------------------------------

operations = [
    # addr
    lambda A, B, registers: registers[A] + registers[B],
    # addi
    lambda A, B, registers: registers[A] + B,

    # mulr
    lambda A, B, registers: registers[A] * registers[B],
    # muli
    lambda A, B, registers: registers[A] * B,

    # banr
    lambda A, B, registers: registers[A] & registers[B],
    # bani
    lambda A, B, registers: registers[A] & B,

    # borr
    lambda A, B, registers: registers[A] | registers[B],
    # bori
    lambda A, B, registers: registers[A] | B,

    # setr
    lambda A, B, registers: registers[A],
    # seti
    lambda A, B, registers: A,

    # gtir
    lambda A, B, registers: int(A > registers[B]),
    # gtri
    lambda A, B, registers: int(registers[A] > B),
    # gtrr
    lambda A, B, registers: int(registers[A] > registers[B]),

    # eqir
    lambda A, B, registers: int(A == registers[B]),
    # eqri
    lambda A, B, registers: int(registers[A] == B),
    # eqrr
    lambda A, B, registers: int(registers[A] == registers[B]),
]

# ----------------------------------------------------------------

import ast

num_behaves_like_three_or_more_opcodes = 0
operations_map_exclusive = [set(range(len(operations))) for op in operations]
possible_opcodes_per_opindex = [set() for op in operations]

for before, op, after, newline in zip(*[iter(data_raw)]*4):
    registers_before = ast.literal_eval(before.lstrip('Before: '))
    opcode, A, B, C = [int(x) for x in op.split(' ')]
    registers_after = ast.literal_eval(after.lstrip('After: '))

    num_possible_operations = 0
    for opindex, operation in enumerate(operations):
        registers = registers_before.copy()
        registers[C] = operation(A, B, registers)
        if registers == registers_after:
            possible_opcodes_per_opindex[opindex].add(opcode)
            num_possible_operations += 1
    num_behaves_like_three_or_more_opcodes += num_possible_operations >= 3

print('result part one:', num_behaves_like_three_or_more_opcodes)


# reduce info to a op dictionary
operations_map = {}
while any(len(possible_opcodes) > 0 for possible_opcodes in possible_opcodes_per_opindex):
    for opindex, possible_opcodes in enumerate(possible_opcodes_per_opindex):
        if len(possible_opcodes) != 1:
            continue
        opcode = possible_opcodes.pop()
        operations_map[opcode] = operations[opindex]
        for possible_opcodes2 in possible_opcodes_per_opindex:
            try:
                possible_opcodes2.remove(opcode)
            except:
                pass

# execute program
registers = [0, 0, 0, 0]
for instruction in program:
    opcode, A, B, C = [int(x) for x in instruction.split(' ')]
    registers[C] = operations_map[opcode](A, B, registers)
print('result part two:', registers)