"""
CP1404/CP5632 - Practical
Get a password with minimum length and display asterisks
"""

MINIMUM_LENGTH = 4

def main():

    def get_valid_password():
        """Get a password of valid size and print asterisks."""
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
        while len(password) < MINIMUM_LENGTH:
            password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
        print('*' * len(password))

    return get_valid_password()

main()