"""
Email to Name Dictionary
Estimate: 30 minutes
Actual: 43 minutes
"""


def main():
    """Display user emails and names."""
    email_to_name = {}

    email = input("Email: ")
    while email != "":
        name = extract_name_from_email(email)
        response = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if response != "" and response != "y":
            name = input("Name: ")

        email_to_name[email] = name
        email = input("Email: ")

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")



def extract_name_from_email(email):
    """Pull out name from ones email"""
    username = email.split('@')[0]
    parts = username.split('.')
    name = " ".join(parts).title()
    return name




main()