#-*- coding: utf-8 -*-

from copy import copy


# ADDITION
def addr(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = registers[a] + registers[b]
    return new_registers

def addi(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = registers[a] + b
    return new_registers

# MULTIPLICATION
def mulr(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = registers[a] * registers[b]
    return new_registers

def muli(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = registers[a] * b
    return new_registers

# BITWISE AND
def banr(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = registers[a] & registers[b]
    return new_registers

def bani(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = registers[a] & b
    return new_registers

# BITWISE OR
def borr(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = registers[a] | registers[b]
    return new_registers

def bori(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = registers[a] | b
    return new_registers

# ASSIGNMENT
def setr(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = registers[a]
    return new_registers

def seti(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = a
    return new_registers

# GREATER-THAN TESTING
def gtir(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = 1 if a > registers[b] else 0
    return new_registers

def gtri(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = 1 if registers[a] > b else 0
    return new_registers

def gtrr(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = 1 if registers[a] > registers[b] else 0
    return new_registers

# EQUALITY TESTING
def eqir(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = 1 if a == registers[b] else 0
    return new_registers

def eqri(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = 1 if registers[a] == b else 0
    return new_registers

def eqrr(registers, a, b, c):
    new_registers = copy(registers)
    new_registers[c] = 1 if registers[a] == registers[b] else 0
    return new_registers



all_operations = {
    "addr": addr, "addi": addi,
    "mulr": mulr, "muli": muli,
    "banr": banr, "bani": bani,
    "borr": borr, "bori": bori,
    "setr": setr, "seti": seti,
    "gtir": gtir, "gtri": gtri, "gtrr": gtrr,
    "eqir": eqir, "eqri": eqri, "eqrr": eqrr,
}