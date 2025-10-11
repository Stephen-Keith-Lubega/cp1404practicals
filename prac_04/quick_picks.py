"""
CP1404/CP5632 Practical
Pick generator
"""
import random

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45
NUMBERS_PER_PICK = 6

number_of_quick_picks = int(input("How many quick picks: "))

for i in range(number_of_quick_picks):
    quick_pick = []
    while len(quick_pick) < NUMBERS_PER_PICK:
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        if number not in quick_pick:
            quick_pick.append(number)

    quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))