#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import sys


def in_range(n, min, max):
    if n < min:
        return False
    if n > max:
        return False
    return True


def in_some_category_range(n, categories):
    for cat in categories:
        if in_category_range(n, categories, cat):
            return True
    return False

def in_category_range(n, categories, cat):
    range1, range2 = categories[cat]
    if in_range(n, range1[0], range1[1]):
        return True
    if in_range(n, range2[0], range2[1]):
        return True
    return False

def are_categories_assigned(categories):
    for cat, indeces in categories.items():
        if len(indeces) > 1:
            return False
    return True

def star1(categories_ranges, nearby_tickets):
    print('PART 1')
    error_rate = 0

    for t in nearby_tickets:
        for n in t:
            error_rate = error_rate + n \
                if not in_some_category_range(n, categories_ranges) else error_rate

    print(f'Error rate = {error_rate}')

def star2(categories_ranges, nearby_tickets, my_ticket):
    valid_tickets = []
    for t in nearby_tickets:
        if all(in_some_category_range(n, categories_ranges) for n in t):
            valid_tickets.append(t)

    categories_indeces = dict(list((cat, set()) for cat in categories_ranges))

    # Each category contains a set of possible ticket indeces
    t = valid_tickets[0]
    for i,n in enumerate(t):
        for cat in categories_ranges:
            if in_category_range(n, categories_ranges, cat):
                categories_indeces[cat].add(i)

    for t in valid_tickets[1:]:
        for cat in categories_ranges:
            cat_indeces = set()
            for i,n in enumerate(t):
                if in_category_range(n, categories_ranges, cat):
                    cat_indeces.add(i)
            categories_indeces[cat] &= cat_indeces

    # Remove duplicates
    while not are_categories_assigned(categories_indeces):
        for cat,indeces in categories_indeces.items():
            if len(indeces) > 1:
                continue
            for _,indeces2 in categories_indeces.items():
                if len(indeces2) > 1:
                    indeces2 -= indeces

    departure_fields_total = 1
    for cat,indeces in categories_indeces.items():
        if 'departure' not in cat:
            continue
        index = int(next(iter(indeces)))
        departure_fields_total *= my_ticket[index]

    print('PART 2')
    print(f'{"CATEGORY NAME" : <20}\tINDEX')
    for cat,index in sorted(categories_indeces.items()):
        print(f'{cat : <20}\t{index}')

    print(f'\nTotal product of departure fields = {departure_fields_total}')



def main(input_file):
    with open(input_file, 'r') as f:
        lines = f.read().split('\n\n')


    categories, my_ticket, nb_tickets = lines

    # Parse categories
    category_re = r'(.*): (\d*)-(\d*) or (\d*)-(\d*)'
    categories_ranges = {}

    for c in categories.split('\n'):
        cat_name, min1, max1, min2, max2 = re.match(category_re, c).groups()
        categories_ranges[cat_name] = [(int(min1), int(max1)), (int(min2), int(max2))]

    # Parse my ticket
    my_ticket = [int(x) for x in my_ticket.split('\n')[-1].split(',')]

    # Parse nearby tickets
    nearby_tickets = []
    for line in nb_tickets.split('\n')[1:]:
        nearby_tickets.append([int(x) for x in line.split(',')])


    star1(categories_ranges, nearby_tickets)

    print('\n--------------------------------------------------\n')

    star2(categories_ranges, nearby_tickets, my_ticket)


if __name__ == "__main__":
    main(sys.argv[1])
