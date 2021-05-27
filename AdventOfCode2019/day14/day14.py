#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from copy import deepcopy
from math import ceil


class ReactionComponent:
    def __init__(self, units, element):
        self.units = units
        self.element = element

    def __repr__(self):
        return f'({self.units}, {self.element})'

    @classmethod
    def from_descr(cls, descr):
        units, element = descr.split()
        return ReactionComponent(int(units), element)


class Reaction:
    def __init__(self, reactives, product):
        self.reactives = reactives
        self.product = product

    def __repr__(self):
        return f'{self.reactives} => {self.product}'
        
    @classmethod
    def from_descr(cls, descr):
        reactives_descr, product_descr = descr.split(' => ')
        reactives = [ReactionComponent.from_descr(r) for r in reactives_descr.split(', ')]
        product = ReactionComponent.from_descr(product_descr)

        return Reaction(reactives, product)

    def is_basic(self):
        return len(self.reactives) == 1 and self.reactives[0].element == 'ORE'


def consume_reserves(component, element_reserves):
    component_after_consume = deepcopy(component)
    for reserve in element_reserves:
        if reserve.element == component.element and component.units > 0:
            units_consumed = min(reserve.units, component.units)
            component_after_consume.units -= units_consumed
            reserve.units -= units_consumed

    return component_after_consume

def update_reserves(component, element_reserves):
    if component.units <= 0:
        return
    for reserve in element_reserves:
        if reserve.element == component.element:
            reserve.units += component.units
            return
    element_reserves.append(component)


def calc_total_ore2(elem, units_needed, all_reactions, element_reserves):
    total_ore = 0
    reaction = all_reactions[elem]
    elem_consumed = consume_reserves(ReactionComponent(units_needed, elem), element_reserves)
    units_needed = elem_consumed.units

    factor = ceil(units_needed / reaction.product.units)
    units_to_consume = factor * reaction.product.units
    units_reserve = units_to_consume - units_needed
    update_reserves(ReactionComponent(units_reserve, elem), element_reserves)

    if reaction.is_basic():
        ore = factor * reaction.reactives[0].units
        return ore

    for reactive in reaction.reactives:
        reactive_units_needed = reactive.units * factor
        total_ore += calc_total_ore2(reactive.element, reactive_units_needed, all_reactions, element_reserves)

    return total_ore


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()

    all_reactions = {}
    element_reserves = []
    for line in lines:
        reaction = Reaction.from_descr(line)
        all_reactions[reaction.product.element] = reaction

    ore = calc_total_ore2('FUEL', 1, all_reactions, element_reserves)
    print('PART 1')
    print(f'Total ORE needed = {ore}')

    print('\n------------------------------------\n')
    print('PART 2')

    ore_reserves = 1000000000000
    low = ore_reserves // ore
    high = low * 2
    element_reserves = []
    mid = 1
    while low < high-1:
        mid = (high + low) // 2
        # print(f'{high} - {low} => {mid}')
        ore = calc_total_ore2('FUEL', mid, all_reactions, element_reserves)

        if ore > ore_reserves:
            high = mid
        elif ore < ore_reserves:
            low = mid
        else:
            break

    ore_high = calc_total_ore2('FUEL', mid, all_reactions, element_reserves)
    if ore_high > ore_reserves:
        mid -= 1
    print(f'Max amount of FUEL produced with {int(ore_reserves)} ORE = {mid}')


if __name__ == "__main__":
    main(sys.argv[1])
