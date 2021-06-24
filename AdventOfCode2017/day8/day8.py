#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from collections import defaultdict
from operator import itemgetter
import re


def get_max_entry(variables):
    return max(variables.items(), key=itemgetter(1))


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    variables = defaultdict(int)
    instruction_format = re.compile(r'(.*) (.*) (.*) if (.*?) (.*)')
    operations = {'inc': '+', 'dec': '-'}
    max_variable_value = ('', 0)

    for line in lines:
        groups = instruction_format.match(line).groups()
        var1, op, number, var2, condition = groups
        var1_access = f"variables['{var1}']"
        var2_access = f"variables['{var2}']"
        instruction = f"{var1_access} = {var1_access} {operations[op]} {number} if {var2_access} {condition} else {var1_access}"
        exec(instruction)
        current_max = get_max_entry(variables)
        if current_max[1] > max_variable_value[1]:
            max_variable_value = current_max

    print(f'Dictionary of registers: {dict(variables)}')
    print(f'PART 1 - Register with biggest value = {get_max_entry(variables)}')
    print(f'PART 2 - Register with max value in any moment = {max_variable_value}')


if __name__ == "__main__":
    main(sys.argv[1])
