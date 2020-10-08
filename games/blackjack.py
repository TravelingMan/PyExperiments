#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Blackjack
Because everyone needs to code a card game
"""

from random import randint


class Blackjack():
    def __init__(self):
        self.deck = []
        self.suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
        self.values = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A')

    def make_deck(self):
        for suit in self.suits:
            for value in self.values:
                self.deck.append((value, suit))

    def pull_card(self):
        return self.deck.pop(randint(0, len(self.deck) - 1))


class Player():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def show_hand(self, dealer_start=True):
        print(f'\n{self.name}')
        print('==============')
        for i in range(len(self.hand)):
            if self.name == 'Dealer' and i == 0 and dealer_start:
                print('- of -')  # Hide first card
            else:
                card = self.hand[i]
                print(f'{card[0]} of {card[1]}')

    def calc_hand(self, dealer_start=True):
        total = 0
        aces = 0
        card_values = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10, "A": 11}
        if self.name == 'Dealer' and dealer_start:
            card = self.hand[1]
            return card_values[card[0]]
        for card in self.hand:
            if card[0] == 'A':
                aces += 1
            else:
                total += card_values[card[0]]
        for i in range(aces):
            if total + 11 > 21:
                total += 1
            else:
                total += 11
        return total


game = Blackjack()
game.make_deck()

name_in = input('What is your name? ')
player = Player(name_in)
dealer = Player('Dealer')

for i in range(2):
    player.add_card(game.pull_card())
    dealer.add_card(game.pull_card())

# TODO: DRY this out eventually with refactor
player.show_hand()
dealer.show_hand()

player_bust = False
dealer_bust = False

# TODO: Build out an actual game loop
# TODO: Track currency
while input('Would you like to stay or hit?').lower() != 'stay':
    player.add_card(game.pull_card())

    player.show_hand()
    dealer.show_hand()

    if player.calc_hand() > 21:
        player_bust = True
        print('You lose!')
        break

if not player_bust:
    while dealer.calc_hand(False) < 17:
        dealer.add_card(game.pull_card())

        if dealer.calc_hand(False) > 21:
            dealer_bust = True
            print('You win!')
            break

player.show_hand()
dealer.show_hand()

if player_bust:
    print('\nYou busted. Better luck next time.')
elif dealer_bust:
    print('\nThe dealer busted. You win!')
elif dealer.calc_hand(False) > player.calc_hand():
    print('\nYou beat the dealer! You win!')
else:
    print('\nYou pushed, no one wins.')