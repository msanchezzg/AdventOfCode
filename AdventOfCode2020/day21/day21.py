#!/usr/bin/python3
#-*- coding: utf-8 -*-

from collections import Counter, OrderedDict
import re
import sys


def star1(allergens, all_ingredients):
    ingredients_counter = Counter(all_ingredients)
    total = 0
    non_alergic_ingrs = []
    for ingr, times in ingredients_counter.items():
        if all(ingr not in allergens[a] for a in allergens):
            total += times
            non_alergic_ingrs.append(ingr)

    print(f'Non-allergic ingredients: {non_alergic_ingrs}')
    print(f'Total = {total}')

def allergens_assigned(allergens):
    for _, ingredients in allergens.items():
        if len(ingredients) > 1:
            return False
    return True

def star2(allergens):
    while not allergens_assigned(allergens):
        for allergen1, ingredients1 in allergens.items():
            if len(ingredients1) == 1:
                ingr = next(iter(ingredients1))
                for allergen2, ingredients2 in allergens.items():
                    if ingr in ingredients2 and allergen1 != allergen2:
                        allergens[allergen2].remove(ingr)

    sorted_allergens = OrderedDict(sorted(allergens.items()))
    canonical_ingr_list = ''
    
    print(f'{"ALLERGEN":<20}\tINGREDIENT')
    for allerg, ingr in sorted_allergens.items():
        i = next(iter(ingr))
        print(f'{allerg:<20}\t{i}')
        canonical_ingr_list += i
        canonical_ingr_list += ','

    canonical_ingr_list = canonical_ingr_list[:-1]
    print()
    print(f'Canonical dangerous ingredient list = {canonical_ingr_list}')

def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()

    line_re = r'(.*) \(contains (.*)\)'
    allergens = {}
    all_ingredients = []

    for line in lines:
        ingrs, allergs = re.match(line_re, line).groups()
        ingrs = ingrs.split(' ')
        allergs = allergs.split(', ')

        all_ingredients += ingrs
        for a in allergs:
            if a in allergens:
                allergens[a] &= set(ingrs)
            else:
                allergens[a] = set(ingrs)

    print('PART 1')
    star1(allergens, all_ingredients)

    print('\n-------------------------------------\n')
    print('PART 2')
    star2(allergens)


if __name__ == "__main__":
    main(sys.argv[1])
