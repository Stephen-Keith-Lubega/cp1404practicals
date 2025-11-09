"""
Guitar management program that reads, displays, sorts, and saves guitars.
"""
from guitar import Guitar


def main():
    """Main program to manage guitar collection."""
    guitars = load_guitars("guitars.csv")
    print(f"Loaded {len(guitars)} guitars.")

    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    add_new_guitars(guitars)
    save_guitars("guitars.csv", guitars)
    print(f"\n{len(guitars)} guitars saved to guitars.csv")


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')
            guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display all guitars."""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """Get user input for new guitars and add to list."""
    print("\nAdd new guitars (blank name to finish):")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Save guitars to a CSV file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


main()