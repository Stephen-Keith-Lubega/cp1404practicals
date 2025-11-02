"""
Test program for Guitar class.
Estimated time: 10 minutes
Actual time:
"""

from prac_06.guitar import Guitar


def main():
    """Test Guitar class methods."""

    # Create two test guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 1000.00)

    # Test get_age()
    print(f"{guitar1.name} get_age() - Expected 100. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected 9. Got {guitar2.get_age()}")

    # Test is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected True. Got {guitar1.determine_weather_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected False. Got {guitar2.determine_weather_vintage()}")


main()