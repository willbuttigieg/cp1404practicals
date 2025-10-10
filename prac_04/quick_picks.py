"""
CP1404 Practical
Quick Picks
"""

import random

NUMBER_OF_RANDOM_NUMBERS = 6
LOWER_LIMIT = 1
UPPER_LIMIT = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    quick_pick = []
    for j in range(NUMBER_OF_RANDOM_NUMBERS):
        pick = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        while pick in quick_pick:
            pick = random.randint(LOWER_LIMIT, UPPER_LIMIT)
        quick_pick.append(pick)
    quick_pick.sort()
    print(" ".join(f"{pick:2}" for pick in quick_pick))