"""
CP1404/CP5632 - Practical
Score_menu
"""


def main():

    print("Welcome!")
    current_score = get_valid_score()
    print_menu()
    choice = input("Enter your choice: ").upper()
    while choice != 'Q':
        if choice == 'G':
            current_score = get_valid_score()
        elif choice == 'P':
            print_result(current_score)
        elif choice == 'S':
            show_stars(current_score)
        else:
            print("Invalid choice")
        print_menu()
        choice = input("Enter your choice: ").upper()
    print("Farewell")


def get_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Good"
    elif score >= 70:
        return "Satisfactory"
    elif score >= 50:
        return "Pass"
    else:
        return "Fail"


def get_valid_score():
    score = float(input("Enter a score (0-100): "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100 inclusive.")
        score = float(input("Enter a score (0-100): "))
    return score


def print_result(score):
    result = get_result(score)
    print(result)


def show_stars(score):
    star_count = int(score)
    print("*" * star_count)


def print_menu():
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


main()