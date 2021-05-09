#!/usr/bin/python3
#-*- coding: utf-8 -*-

from copy import deepcopy
import sys


class Player():
    def __init__(self, id, cards):
        self.id = id
        self.cards = cards

    def __repr__(self):
        return f'Player {self.id}: {self.cards}'

    def __eq__(self, other):
        if not isinstance(other, Player):
            return False
        return self.id == other.id # and self.cards == other.cards

    def top_card(self):
        card = self.cards.pop(0)
        return card

    def add_card(self, card):
        self.cards.append(card)

    def empty_deck(self):
        return self.cards == []

    def get_deck_points(self):
        points = 0
        n_cards = len(self.cards)
        for i, card in enumerate(self.cards):
            points += (n_cards - i) * card

        return points

def star1(player1, player2):
    round_index = 0
    winner = None

    while winner is None:
        round_index += 1
        card1 = player1.top_card()
        card2 = player2.top_card()
        
        round_winner = player1 if card1 > card2 else player2

        if round_winner == player1:
            player1.add_card(card1)
            player1.add_card(card2)
        else:
            player2.add_card(card2)
            player2.add_card(card1)
        
        if player1.empty_deck():
            winner = player2
        elif player2.empty_deck():
            winner = player1

    return winner, round_index


def star2(player1, player2):

    round_index = 0
    winner = None
    game_history = set()

    while winner is None:
        round_index += 1

        # Check if decks statuses already happened
        game_status = (tuple(player1.cards), tuple(player2.cards))
        if game_status in game_history:
            winner = player1
            break

        game_history.add(game_status)

        card1 = player1.top_card()
        card2 = player2.top_card()

        # Check if each player has at least as many cards as indicates the top card
        # (Recursive game)
        if len(player1.cards) >= card1 and len(player2.cards) >= card2:
            new_player1 = Player(player1.id, player1.cards[:card1])
            new_player2 = Player(player2.id, player2.cards[:card2])
            round_winner, _ = star2(new_player1, new_player2)

        # If a player does not have at least as many cards as indicates the top card,
        # Normal round (the player with the biggest card wins)
        else:
            round_winner = player1 if card1 > card2 else player2

        if round_winner == player1:
            player1.add_card(card1)
            player1.add_card(card2)
        else:
            player2.add_card(card2)
            player2.add_card(card1)

        if player1.empty_deck():
            winner = player2
        elif player2.empty_deck():
            winner = player1

    return winner, round_index



def main(input_file):

    with open(input_file, 'r') as f:
        lines = f.read().split('\n\n')

    players = []
    players2 = []

    for group in lines:
        group = group.split('\n')
        player_id = int(group[0].split(' ')[1][:-1])
        player_cards = [int(x) for x in group[1:] if x]
        players.append(Player(player_id, player_cards))
        players2.append(Player(player_id, deepcopy(player_cards)))

    player1, player2 = players    

    print('PART 1')
    winner, round_index = star1(player1, player2)
    winner_points = winner.get_deck_points()
    print(f'Winner: {winner}\nRounds to win = {round_index}\nPoints = {winner_points}')

    print('\n-----------------------------\n')

    player1, player2 = players2
    print('PART 2')
    winner, round_index= star2(player1, player2)
    winner_points = winner.get_deck_points()
    print(f'Winner: {winner}\nRounds to win = {round_index}\nPoints = {winner_points}')

 


if __name__ == "__main__":
    main(sys.argv[1])
