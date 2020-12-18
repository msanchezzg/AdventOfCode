#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys
from stack import Stack


def infix_to_postfix(expression, precedence='normal'):
    # characters = list(expression.replace(' ', ''))
    precedences = {
        'equal': {'+': 0, '-': 0, '*': 0, '/': 0, '(': -1},
        'normal': {'+': 0, '-': 0, '*': 1, '/': 1, '(': -1},
        'reverse': {'+': 1, '-': 1, '*': 0, '/': 0, '(': -1}
    }
    if precedence not in precedences:
        raise ValueError("Precedence argument must be one of ['normal', 'equal', 'reverse']")

    operands_precedence = precedences[precedence]
    characters = list(expression)
    postfix = ""
    stack = Stack()

    for c in characters:
        if c.isdigit():
            postfix += c
        elif c == ' ':
            postfix += c
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while not stack.is_empty() and stack.top() != '(':
                top = stack.pop()
                postfix += ' '
                postfix += top
            if not stack.is_empty() and stack.top() == '(':
                stack.pop()

        elif c in operands_precedence:   # Operator
            while not stack.is_empty() and \
                operands_precedence[c] <= operands_precedence[stack.top()]:
                postfix += ' '
                postfix += stack.pop()

            stack.append(c)

    while not stack.is_empty():
        postfix += ' '
        postfix += stack.pop()

    return postfix

def evaluate_posfix_expression(expression):
    elements = [x for x in expression.split(' ') if x]
    operands = ['+', '-', '*', '/']
    stack = Stack()

    for e in elements:
        if e.isdigit():
            stack.append(e)
        elif e in operands:
            n1 = stack.pop()
            n2 = stack.pop()
            res = str(eval(n1 + e + n2))
            stack.append(res)

    return int(stack.pop())


def star1(expressions):
    total = 0
    for expression in expressions:
        postfix = infix_to_postfix(expression, precedence='equal')
        res = evaluate_posfix_expression(postfix)
        print(f'{expression} = {res}')
        total += res

    print()
    print(f'Sum of all results = {total}')

def star2(expressions):
    total = 0
    for expression in expressions:
        postfix = infix_to_postfix(expression, precedence='reverse')
        res = evaluate_posfix_expression(postfix)
        print(f'{expression} = {res}')
        total += res

    print()
    print(f'Sum of all results = {total}')


def main(input_file):
    with open(input_file, 'r') as f:
        lines = [x.strip() for x in f.readlines() if x]

    print('PART 1')
    star1(lines)

    print('\n----------------------------\n')

    print('PART 2')
    star2(lines)


if __name__ == "__main__":
    main(sys.argv[1])
