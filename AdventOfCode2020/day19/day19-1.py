#!/usr/bin/python3
#-*- coding: utf-8 -*-

import itertools
import re
import sys


def get_children(rules_dependencies, rule):
    if rule not in rules_dependencies:
        return [rule]
    children = [rule]
    for option in rules_dependencies[rule]:
        for child in option:
            children += get_children(rules_dependencies, child)
    return children

def star1(rules, lines):

    rule_string_re  = r'^(\d*): "(\w)"$'
    rule_num_re = r'^(\d*): (.*)$'

    rules_patterns = {}
    rules_to_build = {}
    rules_completed = []

    for r in rules:
        if re.match(rule_string_re, r):
            rule_num, rule_str = re.match(rule_string_re, r).groups()
            rule_num = int(rule_num)
            rules_completed.append(rule_num)
            rules_patterns[rule_num] = [rule_str]
        elif re.match(rule_num_re, r):
            rule_num, rule_str = re.match(rule_num_re, r).groups()
            rule_num = int(rule_num)
            rule_options = rule_str.split('|')
            options = []
            for ro in rule_options:
                nums = [int(x) for x in ro.split(' ') if x]
                options.append(nums)

            rules_to_build[rule_num] = options

    children_of_rule0 = set(get_children(rules_to_build, 0))

    # Converting rules into patterns
    while len(rules_completed) != len(rules):
        for rule_num, rule_options in rules_to_build.items():
            if rule_num in rules_patterns:
                continue
            if rule_num not in children_of_rule0:
                continue

            rule_completed = True
            options = []

            for option in rule_options:
                if all(num in rules_patterns for num in option):
                    option_patterns = [rules_patterns[num] for num in option]
                    patterns_permutations = list(itertools.product(*option_patterns))
                    for perm in patterns_permutations:
                        options.append(''.join(perm))
                else:
                    rule_completed = False
                    break

            if rule_completed:
                rules_completed.append(rule_num)
                rules_patterns[rule_num] = options

    # Checking lines against patterns
    rule_0_patterns = set(rules_patterns[0])
    num_patterns = len(rule_0_patterns)

    matched_strings = set()
    for i,patt in enumerate(rule_0_patterns,1):
        print(f'pattern {i}/{num_patterns}')
        regex = re.compile('^'+patt+'$')
        for l in lines:
            if regex.match(l):
                matched_strings.add(l) 

    print(f'Lines that match Rule 0 = {len(matched_strings)}')


def main(input_file):

    with open(input_file, 'r') as f:
        rules, lines = f.read().split('\n\n')

    rules = [r for r in rules.split('\n') if r]
    lines = [l for l in lines.split('\n') if l]
    print('PART 1')
    star1(rules, lines)


if __name__ == "__main__":
    main(sys.argv[1])