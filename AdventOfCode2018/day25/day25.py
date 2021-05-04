#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
from copy import copy
from stars import Star, Constellation


def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.readlines()

    stars_not_in_const = []
    for line in lines:
        x, y, z, w = [int(a) for a in line.split(',')]
        stars_not_in_const.append(Star(x, y, z, w))

    constellations = []
    while len(stars_not_in_const) > 0:

        # Create new const
        new_const = Constellation()
        new_const.add_star(stars_not_in_const.pop(0))

        for star in new_const.stars:
            # add to the constellation all non-placed stars
            # which are in distance with a star of the constellation

            # search for nearby stars
            remaining_stars = copy(stars_not_in_const)
            for star2 in stars_not_in_const:
                if star.manhattan_dist(star2) <= 3:
                    new_const.add_star(star2)
                    remaining_stars.remove(star2)

                stars_not_in_const = remaining_stars

        constellations.append(new_const)


    print('PART 1')
    print('List of constellations:')
    for i, c in enumerate(constellations):
        print(f'- Constellation {i}: {c}')

    print()
    print(f'Number of constellations = {len(constellations)}')


if __name__ == "__main__":
    main(sys.argv[1])
