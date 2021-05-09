import re
from enum import Enum


class GameStatus(Enum):
    PLAYING = 0
    WINNER = 1
    DRAW = 2

class Group:
    def __init__(self, units, hit_points, weaknesses, immunities, attack_damage, attack_type, initiative, id, team=None):
        self.units = units
        self.units_remaining = units
        self.hit_points = hit_points
        self.weaknesses = weaknesses
        self.immunities = immunities
        self.attack_damage = attack_damage
        self.attack_type = attack_type
        self.initiative = initiative
        self.id = id
        self.team = team
        self.is_target = False

    def __repr__(self):
        return str(self.__dict__)

    def __hash__(self):
        return hash((self.team, self.id))

    @staticmethod
    def from_description(descr, id):
        group_descr_format = re.compile(r'(?P<units>\d+) units each with (?P<hit_p>\d+) hit points (\((?P<powers>.+)\) )?with' +
            r' an attack that does (?P<att_dam>\d+) (?P<att_type>.*) damage at initiative (?P<initiative>\d+)')
        weakness_format = re.compile(r'weak to (.*)')
        immunity_format = re.compile(r'immune to (.*)')
        group_match = group_descr_format.match(descr)
        if not group_match:
            raise ValueError(f'Argument does not match group description format: {descr}')

        units = int(group_match.group('units'))
        hit_points = int(group_match.group('hit_p'))
        attack_damage = int(group_match.group('att_dam'))
        attack_type = group_match.group('att_type')
        initiative = int(group_match.group('initiative'))
        powers = group_match.group('powers')
        weaknesses = []
        immunities = []
        if powers is not None:
            for p in powers.split('; '):
                weakness_match = weakness_format.match(p)
                if weakness_match:
                    for w in weakness_match.group(1).split(', '):
                        weaknesses.append(w)

                immunities_match = immunity_format.match(p)
                if immunities_match:
                    for w in immunities_match.group(1).split(', '):
                        immunities.append(w)

        return Group(units, hit_points, weaknesses, immunities, attack_damage, attack_type, initiative, id)

    def effective_power(self):
        return self.units_remaining * self.attack_damage

    def damage_to_deal(self, rival_group):
        if rival_group is None:
            return 0
        damage = self.effective_power()
        if self.attack_type in rival_group.immunities:
            damage = 0
        elif self.attack_type in rival_group.weaknesses:
            damage *= 2
        return damage

    def choose_target(self, rival_team, debug=True):
        max_damage = 0
        target_group = None
        if self.units_remaining > 0:
            for group in rival_team.groups:
                if group.is_target:
                    continue
                damage = self.damage_to_deal(group)
                if damage > max_damage:
                    target_group = group
                    max_damage = damage
                elif damage == max_damage and max_damage != 0:
                    if group.effective_power() > target_group.effective_power():
                        target_group = group
                        max_damage = damage
                    elif group.effective_power() == target_group.effective_power():
                        if group.initiative > target_group.initiative:
                            target_group = group
                            max_damage = damage
        if target_group is not None:
            target_group.is_target = True

        target_group_id = target_group.id if target_group is not None else 'None'

        if debug:
            print(f'{self.team.name} group {self.id} would deal defending group {target_group_id} ' +
                    f'{self.damage_to_deal(target_group)} damage'
                )

        return target_group

    def attack(self, rival_group, debug=True):
        if rival_group is None:
            return 0
        if not isinstance(rival_group, Group):
            return 0
        if self.units_remaining <= 0:
            return 0

        damage = self.damage_to_deal(rival_group)
        units_dead = rival_group.receive_attack(damage)

        if debug:
            print(f'{self.team.name} group {self.id} attacks defending group {rival_group.id}, ' +
                    f'killing {units_dead} units (damage={damage})'
                )

        return units_dead

    def receive_attack(self, damage):
        if self.units_remaining <= 0:
            return 0

        units_dead = damage // self.hit_points
        self.units_remaining -= units_dead
        if self.units_remaining < 0:
            units_dead += self.units_remaining
            self.units_remaining = 0
        return units_dead

    def is_alive(self):
        return self.units_remaining > 0


class Team:
    def __init__(self, name):
        self.name = name
        self.groups = []

    def __repr__(self):
        return str(self.groups)

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        if not isinstance(other, Team):
            return False
        return self.name == other.name

    @staticmethod
    def from_description(descr):
        team_name, *team_groups = descr.split('\n')
        team = Team(team_name)
        for i, gr in enumerate(team_groups, 1):
            team.add_group(Group.from_description(gr, i))

        return team

    def pretty_print(self):
        print(f'{self.name}:')
        if len(self.groups) == 0:
            print('No groups remain.')
        else:
            for group in self.groups:
                print(f'Group {group.id} contains {group.units_remaining} units')

    def add_group(self, group):
        if not isinstance(group, Group):
            raise TypeError
        self.groups.append(group)
        group.team = self

    def remove_group(self, group_id):
        for i, group in enumerate(self.groups):
            if group.id == group_id:
                self.groups.pop(i)
                break

    def remove_dead_groups(self):
        for group in self.groups:
            if not group.is_alive():
                self.remove_group(group.id)

    def get_units_remaining(self):
        units = 0
        for group in self.groups:
            units += group.units_remaining
        return units

    def reset_targets(self):
        for group in self.groups:
            group.is_target = False

    def is_alive(self):
        for group in self.groups:
            if group.is_alive():
                return True
        return False

    def boost(self, booster):
        for group in self.groups:
            group.attack_damage += booster


class Game:
    def __init__(self, team1, team2):
        self.team1 = team1
        self.team2 = team2
        self.status = GameStatus.PLAYING

    def print_teams_status(self):
        self.team1.pretty_print()
        self.team2.pretty_print()

    def get_target_selection_order(self):
        groups = self.team1.groups + self.team2.groups
        sorted_groups = sorted(groups, key=lambda g: (-g.effective_power() , -g.initiative))
        return sorted_groups

    def get_attack_order(self):
        groups = self.team1.groups + self.team2.groups
        sorted_groups = sorted(groups, key=lambda g: -g.initiative)
        return sorted_groups

    def play(self, debug=True):
        while self.status == GameStatus.PLAYING:
            if debug:
                print('-----------------ROUND-----------------')
                self.print_teams_status()
                print()

            self.round(debug=debug)
            if debug:
                print()

        if debug:
            print('-----------------END-----------------')
            self.print_teams_status()

        if self.status == GameStatus.DRAW:
            return None
        return self.team1 if self.team1.is_alive() else self.team2

    def round(self, debug=True):
        # MARK GROUPS AS NOT TARGETED
        self.team1.reset_targets()
        self.team2.reset_targets()

        # TARGET SELECTION PHASE
        target_selection_order = self.get_target_selection_order()
        groups_targets = {}
        for group in target_selection_order:
            rival_team = self.team1 if group.team == self.team2 else self.team2
            groups_targets[group] = group.choose_target(rival_team, debug=debug)

        if debug:
            print()

        # ATTACK PHASE
        attack_order = self.get_attack_order()
        total_units_dead = 0
        for attacker in attack_order:
            target = groups_targets[attacker]
            total_units_dead += attacker.attack(target, debug=debug)

        # REMOVE GROUPS WITH NO REMAINING UNITS
        self.team1.remove_dead_groups()
        self.team2.remove_dead_groups()

        # IF THERE HAVE BEEN NO KILLS, END GAME (DRAW)
        if total_units_dead == 0:
            self.status = GameStatus.DRAW

        # IF A TEAM DOES NOT HAVE GROUPS REMAINING, END GAME (WINNER)
        if not self.team1.is_alive() or not self.team2.is_alive():
            self.status = GameStatus.WINNER
