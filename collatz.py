#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Collatz
A fun math problem.
"""


def collatz(number):
    if number % 2 == 0:
        x = number / 2
        print(x)
        return x
    else:
        x = 3 * number + 1
        print(x)
        return x


def get_number():
    try:
        user_number = int(input('Enter a number: '))
        x = collatz(user_number)

        while x != 1:
            x = collatz(x)
    except ValueError:
        print('Please enter a standard integer (whole number)')
        get_number()


get_number()
