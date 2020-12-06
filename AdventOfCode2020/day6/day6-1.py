#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n\n')

    total_questions = 0
    for group in lines:
        answers = [a for a in list(group) if a != '\n']
        questions = set(answers)
        total_questions += len(questions)

    print(f'Total questions answered yes = {total_questions}')


if __name__ == "__main__":
    main(sys.argv[1])
