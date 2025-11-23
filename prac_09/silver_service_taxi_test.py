"""
CP1404/CP5632 Practical
SilverServiceTaxi class testing
"""
from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test the SilverServiceTaxi class."""

    # Create a SilverServiceTaxi with fanciness of 2
    taxi = SilverServiceTaxi("Silver Taxi", 200, 2)

    # Drive 18 km
    taxi.drive(18)

    # Print details
    print(taxi)
    print(f"Current fare: ${taxi.get_fare():.2f}")

    # Test with assert - fare should be $48.80 (rounded to nearest 10c)
    # 18 km * $1.23 (base rate) * 2 (fanciness) + $4.50 (flagfall)
    # = 18 * 2.46 + 4.50 = 44.28 + 4.50 = 48.78 → rounds to $48.80
    assert taxi.get_fare() == 48.80, f"Expected $48.80 but got ${taxi.get_fare():.2f}"
    print("Assert test passed: 18km trip with fanciness 2 = $48.80 (rounded)")
    print()

    # Test with a Hummer (fanciness of 4)
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    print(f"Current fare: ${hummer.get_fare():.2f}")
    print()

    # Additional test - drive the hummer and check fare
    hummer.drive(10)
    print(f"After driving 10km:")
    print(hummer)
    expected_fare = round(10 * 1.23 * 4, 1) + 4.50  # 49.2 + 4.50 = 53.70
    assert hummer.get_fare() == expected_fare, f"Expected ${expected_fare:.2f} but got ${hummer.get_fare():.2f}"
    print(f"Current fare: ${hummer.get_fare():.2f}")
    print("Assert test passed!")


main()