"""
Wimbledon Champions Data Processing
This program reads wimbledon.csv and displays:
1. Champions and their win counts
2. Countries that have won in alphabetical order

Estimated time: 40 minutes
Actual time: 128minutes
"""


def main():
    """
    Main function to orchestrate reading and displaying Wimbledon data.
    """
    filename = "wimbledon.csv"

    # Read the data
    wimbledon_data = read_wimbledon_data(filename)

    # Process champions
    champions = count_champions(wimbledon_data)

    # Display champions and win counts
    print("Wimbledon Champions:")
    for champion, count in champions.items():
        print(f"{champion} {count}")

    # Process and display countries
    countries = get_countries(wimbledon_data)
    sorted_countries = sorted(countries)
    country_string = ", ".join(sorted_countries)

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(country_string)



def read_wimbledon_data(filename):
    """
    Read the wimbledon.csv file and return a list of lists.
    Each inner list contains the data for one championship.
    """
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data.append(line.strip().split(','))
    return data



def count_champions(data):
    """
    Count how many times each champion has won.
    Returns a dictionary with champion names as keys and win counts as values.
    """
    champion_counts = {}
    for row in data:
        champion = row[2]  # Champion name is in the third column (index 2)
        if champion in champion_counts:
            champion_counts[champion] += 1
        else:
            champion_counts[champion] = 1
    return champion_counts


def get_countries(data):
    """
    Extract all unique countries from the data.
    Returns a set of country codes.
    """
    countries = set()
    for row in data:
        country = row[1]
        countries.add(country)
    return countries


if __name__ == "__main__":
    main()