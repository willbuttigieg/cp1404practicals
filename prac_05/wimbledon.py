"""
CP1404 Practical
Wimbledon
Estimate: 30 minutes
Actual:    minutes
"""

FILENAME = "wimbledon.csv"
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Wimbledon"""
    records = read_file(FILENAME)
    champion_to_count, winning_countries = process_records(records)
    display_records(champion_to_count, winning_countries)


def read_file(filename):
    """Read file and store data as nested lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            data = line.strip().split(",")
            records.append(data)
    return records


def process_records(records):
    """Create dictionary of champions and set of winning countries."""
    champion_to_count = {}
    winning_countries = set()
    for record in records:
        winning_countries.add(record[COUNTRY_INDEX])
        try:
            champion_to_count[record[CHAMPION_INDEX]] += 1
        except KeyError:
            champion_to_count[record[CHAMPION_INDEX]] = 1
    return champion_to_count, winning_countries



def display_records(champion_to_count, winning_countries):
    """Display records in specific format."""
    print("Wimbledon Champions:")
    for champion in champion_to_count.items():
        print(f"{champion[0]} {champion[1]}")
    print()
    print(f"These {len(winning_countries)} countries have won wimbledon:")
    print(", ".join(sorted(winning_countries)))



main()