"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    """Get numeric score and display its status"""

    score = float(input("Enter score: "))
    (determine_status(score))

    random_score = random.randint(0, 100)
    print(f"Random score: {random_score}")
    determine_status(random_score)


def determine_status(score):
    """determine_status"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()