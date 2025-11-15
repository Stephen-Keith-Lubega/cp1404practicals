"""
Guitar collection program.
Estimated time: 25 minutes
Actual time: 50 minutes
"""


from prac_06.guitar import Guitar

def main():
    """Manage the collection of guitars"""
    guitars = []
    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added\n")

    print("\nAll the guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")
