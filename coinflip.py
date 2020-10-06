"""coinflip.py: Simulators 10,000 sets of 100 coin flips to find streaks of 6 or more."""

import random

number_of_streaks = 0
total_heads = 0
total_tails = 0

for experiment_number in range(10000):
    flip = []
    heads = 0
    tails = 0

    for x in range(100):
        coin = random.randint(0, 1)
        if coin == 0:
            flip.append('H')
            tails = 0
            heads += 1
            total_heads += 1
            if heads >= 6:
                print(f'    Heads: {heads} in a row! Test number {experiment_number}')
                number_of_streaks += 1
        else:
            flip.append('T')
            tails += 1
            total_tails += 1
            heads = 0
            if tails >= 6:
                print(f'    Tails: {tails} in a row! Test number {experiment_number}')
                number_of_streaks += 1

print('\nFinished. Totals out of 10,000 sets of 100 coin flips:')
print(f'Heads: {total_heads} | Tails: {total_tails} | Streaks: {number_of_streaks}')
