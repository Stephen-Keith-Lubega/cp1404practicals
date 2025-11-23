"""
CP1404/CP5632 Practical
Taxi simulator program
"""
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Run the taxi simulator."""
    taxis = [Taxi("Prius", 100),
             SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    total_bill = 0.0

    print("Let's drive!")
    menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    while menu_choice != 'q':
        if menu_choice == 'c':
            current_taxi = choose_taxi(taxis)
        elif menu_choice == 'd':
            total_bill += drive_taxi(current_taxi)
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    # Final output when quitting
    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """Display available taxis and let user choose one."""
    print("Taxis available:")
    display_taxis(taxis)

    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None


def drive_taxi(current_taxi):
    """Drive the current taxi and return the trip cost."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0.0

    try:
        distance = float(input("Drive how far? "))
        current_taxi.start_fare()
        current_taxi.drive(distance)
        trip_cost = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
        return trip_cost
    except ValueError:
        print("Invalid distance")
        return 0.0


def display_taxis(taxis):
    """Display all taxis with their index numbers."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


main()