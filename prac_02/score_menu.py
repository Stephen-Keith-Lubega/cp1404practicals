"""
CP1404/CP5632 - Practical
Program to determine score status
"""
def main():
    """Get numeric score and display its status"""

    score = float(input("Enter score: "))
    (determine_status(score))


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