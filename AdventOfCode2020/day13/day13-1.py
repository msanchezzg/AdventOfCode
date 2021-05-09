#!/usr/bin/python3
#-*- coding: utf-8 -*-

import sys


def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.readlines()

    time = int(lines[0])
    buses = [int(x) for x in lines[1].split(',') if x.isdigit()]
    buses_arrivals = []

    for b in buses:
        c = time // b
        r = time % b
        if r == 0:
            buses_arrivals.append((c*b, b))
        else:
            buses_arrivals.append(((c+1)*b, b))

    next_bus_time, next_bus = min(buses_arrivals)
    minutes = next_bus_time - time

    print('PART 1')
    print(f'Next bus is {next_bus} that arrives at {next_bus_time}')
    print(f'Minutes to wait * busID = {minutes} * {next_bus} = {minutes*next_bus}')


if __name__ == "__main__":
    main(sys.argv[1])
