"""
CP1404/CP5632 Practical
UnreliableCar class testing
"""
from prac_09.unreliable_car import UnreliableCar


def main():
    """Test the UnreliableCar class."""

    # Create a very reliable car (should drive most of the time)
    good_car = UnreliableCar("Mostly Good", 100, 90)

    # Create an unreliable car (should drive less often)
    bad_car = UnreliableCar("Mostly Bad", 100, 30)

    # Test over many iterations to see reliability in action
    print("Testing unreliable cars over 10 attempts:")
    print()

    # Test the good car (90% reliability)
    print(f"{good_car.name} (90% reliability):")
    successful_drives = 0
    for i in range(1, 11):
        print(f"Attempting to drive {i}: ", end="")
        distance_driven = good_car.drive(10)
        if distance_driven > 0:
            successful_drives += 1
            print(f"Drove {distance_driven}km - Odometer: {good_car.odometer}km")
        else:
            print("Failed to drive (unreliable)")
    print(f"Success rate: {successful_drives}/10 drives")
    print()

    # Test the bad car (30% reliability)
    print(f"{bad_car.name} (30% reliability):")
    successful_drives = 0
    for i in range(1, 11):
        print(f"Attempting to drive {i}: ", end="")
        distance_driven = bad_car.drive(10)
        if distance_driven > 0:
            successful_drives += 1
            print(f"Drove {distance_driven}km - Odometer: {bad_car.odometer}km")
        else:
            print("Failed to drive (unreliable)")
    print(f"Success rate: {successful_drives}/10 drives")


main()