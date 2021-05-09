#!/usr/bin/python3
#-*- coding: utf-8 -*-


from copy import deepcopy
import sys
import game


def main(input_file):

    with open(input_file, 'r') as f:
        imm, inf = f.read().split('\n\n')

    immune_team_original = game.Team.from_description(imm)
    infection_team_original = game.Team.from_description(inf)
    booster = 100
    while True:
        immune_team = deepcopy(immune_team_original)
        infection_team = deepcopy(infection_team_original)
        immune_team.boost(booster)
        simulator = game.Game(immune_team, infection_team)
        team_winner = simulator.play(debug=False)

        if team_winner == immune_team:
            break
        booster += 1

    print('PART 2')
    print(f'Booster: {booster}')
    print(f'Total units remaining of winner team = {team_winner.get_units_remaining()}')


if __name__ == "__main__":
    main(sys.argv[1])
