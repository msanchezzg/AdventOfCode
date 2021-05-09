#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n\n')

    total_questions = 0
    for group in lines:
        answers_by_person = group.split('\n')
        repeated_questions = set(answers_by_person[0])

        for p in answers_by_person[1:]:
            repeated_questions &= set(p)

        total_questions += len(repeated_questions)

    print(f'Total questions everyone answered yes within a group = {total_questions}')


if __name__ == "__main__":
    main(sys.argv[1])
