#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Dragon Adventure
Adapted from Al Sweigart's "Dragon Realms" game
"""

import random
import time


def display_intro():
    print('''You are in a land of Dragons and valuable loot. Before you,
tucked into the cliffs of a long forgotten mountain, two caves that
clearly belong to the great wyrms await your advance. One of them
holds great treasure and a friendlier dragon. The other, death.\n''')


def choose_cave():
    cave = ''
    while cave != '1' and cave != '2':
        print('Which terrifying cave do you choose? (1 or 2)')
        cave = input()

    return cave


def check_cave(choosen_cave):
    print('\nYou steady yourself and approach the cave.')
    time.sleep(2)
    print('\nDarkness surrounds you. A wave of heat slams into your body.')
    time.sleep(2)
    print('''\nThe eyes of a terrifying dragon suddenly open, lighting the cave with an ominous, ancient light. The 
enormous head approaches you and ...''')
    time.sleep(3)

    friendly_cave = random.randint(1, 2)

    if choosen_cave == str(friendly_cave):
        print('\nOffers you a portion of his treasure!')
    else:
        print('\nSnaps his jaws around you, ending your life.')


play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    display_intro()
    cave_number = choose_cave()
    check_cave(cave_number)

    play_again = input('Want to try your luck again? ')
