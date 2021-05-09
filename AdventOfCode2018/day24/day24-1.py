#!/usr/bin/python3
#-*- coding: utf-8 -*-


import sys
import game


def main(input_file):

    with open(input_file, 'r') as f:
        imm, inf = f.read().split('\n\n')

    immune_team = game.Team.from_description(imm)
    infection_team = game.Team.from_description(inf)
    simulator = game.Game(immune_team, infection_team)
    team_winner = simulator.play()

    print()
    print('PART 1')
    print(f'Total units remaining of winner team = {team_winner.get_units_remaining()}')


if __name__ == "__main__":
    main(sys.argv[1])
