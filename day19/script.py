#!/usr/bin/python3

# test input
# pc = 0
# program_raw = [
#     'seti 5 0 1',
#     'seti 6 0 2',
#     'addi 0 1 0',
#     'addr 1 2 3',
#     'setr 1 0 0',
#     'seti 8 0 4',
#     'seti 9 0 5',
# ]

# puzzle input
pc = 3
program_raw = [line.strip() for line in open('day19/input.txt').readlines()]

# ----------------------------------------------------------------

operations = {
    'addr': lambda A, B, registers: registers[A] + registers[B],
    'addi': lambda A, B, registers: registers[A] + B,

    'mulr': lambda A, B, registers: registers[A] * registers[B],
    'muli': lambda A, B, registers: registers[A] * B,

    'banr': lambda A, B, registers: registers[A] & registers[B],
    'bani': lambda A, B, registers: registers[A] & B,

    'borr': lambda A, B, registers: registers[A] | registers[B],
    'bori': lambda A, B, registers: registers[A] | B,

    'setr': lambda A, B, registers: registers[A],
    'seti': lambda A, B, registers: A,

    'gtir': lambda A, B, registers: int(A > registers[B]),
    'gtri': lambda A, B, registers: int(registers[A] > B),
    'gtrr': lambda A, B, registers: int(registers[A] > registers[B]),

    'eqir': lambda A, B, registers: int(A == registers[B]),
    'eqri': lambda A, B, registers: int(registers[A] == B),
    'eqrr': lambda A, B, registers: int(registers[A] == registers[B]),
}

# ----------------------------------------------------------------

program = [ (int(instr[3]), operations[instr[0]], int(instr[1]), int(instr[2])) for instr in (line.split() for line in program_raw)]

# ----------------------------------------------------------------

registers = [0] * 6
registers[pc] = 0
while registers[pc] < len(program):
    instr = program[registers[pc]]
    registers[instr[0]] = instr[1](instr[2], instr[3], registers)
    registers[pc] += 1
    print(registers[0])

print('result part one:', registers[0])

# ----------------------------------------------------------------

# registers = [0] * 6
# registers[pc] = 0
# registers[0] = 1
# while registers[pc] < len(program):
#     instr = program[registers[pc]]
#     registers[instr[0]] = instr[1](instr[2], instr[3], registers)
#     registers[pc] += 1

# print('result part two:', registers[0])