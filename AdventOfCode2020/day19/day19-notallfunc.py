#!/usr/bin/python3
#-*- coding: utf-8 -*-

import itertools
import re
import sys


def matches_rule_42_1time(string, rule_42_patterns):
    if string == '':
        return string

    for patt_42 in rule_42_patterns:
        regex_42 = re.compile('^'+patt_42+'.*')
        if regex_42.match(string):
            substring = string[len(patt_42):]
            return substring

    return string

def matches_rule_11_1time(string, rule_42_patterns, rule_31_patterns):
    if string == '':
        return string

    for patt_42 in rule_42_patterns:
        regex_42 = re.compile('^'+patt_42+'.*')
        if regex_42.match(string):
            for patt_31 in rule_31_patterns:
                regex_31 = re.compile('^.*'+patt_31+'$')
                if regex_31.match(string):
                    substring = string[len(patt_42):-len(patt_31)]
                    return substring

    return string

def matches_rule_11_ntimes(string, rule_42_patterns, rule_31_patterns):
    if string == '':
        return string

    for patt_42 in rule_42_patterns:
        regex_42 = re.compile('^'+patt_42+'.*')
        if regex_42.match(string):
            for patt_31 in rule_31_patterns:
                regex_31 = re.compile('^.*'+patt_31+'$')
                if regex_31.match(string):
                    substring = string[len(patt_42):-len(patt_31)]
                    return matches_rule_11_ntimes(substring, rule_42_patterns, rule_31_patterns)

    return string

def get_rule_children(rules_dependencies, rule):
    if rule not in rules_dependencies:
        return [rule]

    children = [rule]
    for option in rules_dependencies[rule]:
        for child in option:
            children += get_rule_children(rules_dependencies, child)
    return children

def get_rules_patterns(rules):
    rule_string_re  = r'^(\d*): "(\w)"$'
    rule_num_re = r'^(\d*): (.*)$'
    rules_patterns = {}
    rules_to_build = {}

    # Convert list of rules into rules_to_build: dict of rules and their dependencies
    for rule in rules:
        if re.match(rule_string_re, rule):
            rule_num, rule_str = re.match(rule_string_re, rule).groups()
            rule_num = int(rule_num)
            rules_patterns[rule_num] = [rule_str]
        elif re.match(rule_num_re, rule):
            rule_num, rule_str = re.match(rule_num_re, rule).groups()
            rule_num = int(rule_num)
            rule_options = rule_str.split('|')
            options = []
            for rule_opt in rule_options:
                nums = [int(num) for num in rule_opt.split(' ') if num]
                options.append(nums)

            rules_to_build[rule_num] = options

    # Convert rules into rules_patterns: dict of rules and a list of all their possible patterns.
    while len(rules_patterns) != len(rules):
        for rule_num, rule_options in rules_to_build.items():
            if rule_num in rules_patterns:
                continue

            rule_completed = True
            options = []
            for option in rule_options:
                all_nums_have_patt = True
                option_patterns = []
                for num in option:
                    if num not in rules_patterns:
                        all_nums_have_patt = False
                        break
                    option_patterns.append(rules_patterns[num])
                if not all_nums_have_patt:
                    rule_completed = False
                    break

                patterns_permutations = list(itertools.product(*option_patterns))
                for perm in patterns_permutations:
                    options.append(''.join(perm))
   
            if rule_completed:
                rules_patterns[rule_num] = options

    return rules_patterns

def star1(rules_patterns, lines):
    """
    Rule 0 is formed by rules 8 and 11 === rules 42, and 42 and 31.
    """

    rule_42_patterns = set(rules_patterns[42])
    rule_31_patterns = set(rules_patterns[31])
    matched_strings = set()

    for line in lines:
        match = True
        string = line
        new_string = matches_rule_42_1time(string, rule_42_patterns)
        if string == new_string:
            match = False
        if new_string == '':
            match = False
        if match:
            string = matches_rule_11_1time(new_string, rule_42_patterns, rule_31_patterns)
            if string != '':
                match = False

        if match:
            matched_strings.add(line)

    print(f'Lines that match Rule 0 = {len(matched_strings)}')

def star2(rules_patterns, lines):
    """
    Rule 0 is formed by rules 8 and 11 === rules 42 (n times), and 42 and 31 (m times).
    """

    rule_42_patterns = set(rules_patterns[42])
    rule_31_patterns = set(rules_patterns[31])
    matched_strings = set()

    for line in lines:
        string = line
        while True:
            new_string = matches_rule_42_1time(string, rule_42_patterns)
            if string == new_string:
                match = False
                break
            if new_string == '':
                match = False
                break
            string = matches_rule_11_ntimes(new_string, rule_42_patterns, rule_31_patterns)
            if string == '':
                match = True
                break
            string = new_string

        if match:
            matched_strings.add(line)

    print(f'Lines that match Rule 0 (modified) = {len(matched_strings)}')


def main(input_file):

    with open(input_file, 'r') as f:
        rules, lines = f.read().split('\n\n')

    rules = [r for r in rules.split('\n') if r]
    lines = [line for line in lines.split('\n') if line]

    rules_patterns = get_rules_patterns(rules)

    print('PART 1')
    star1(rules_patterns, lines)

    print('\n----------------------------------------\n')

    print('PART 2')
    star2(rules_patterns, lines)


if __name__ == "__main__":
    main(sys.argv[1])
