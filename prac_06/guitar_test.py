"""
CP1404 Practical 6
Guitar Test Program
"""

from guitar import Guitar


def main():
    """Call test functions."""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2016, 300)
    test_get_age(guitar, another_guitar)
    test_is_vintage(guitar, another_guitar)
    test_str(guitar, another_guitar)


def test_get_age(guitar, another_guitar):
    """Test get_age() method."""
    print(f"{guitar.name} get_age() - expected 103. Got {guitar.get_age()}")
    print(f"{another_guitar.name} get_age() - expected 9. Got {another_guitar.get_age()}")


def test_is_vintage(guitar, another_guitar):
    """Test is_vintage() method."""
    print(f"{guitar.name} is_vintage() - expected True. Got {guitar.is_vintage()}")
    print(f"{another_guitar.name} is_vintage() - expected False. Got {another_guitar.is_vintage()}")


def test_str(guitar, another_guitar):
    """Test str() method."""
    print(f"{guitar.name} str() - expected Gibson L-5 CES (1922): $16,035.40. Got {guitar}.")
    print(f"{another_guitar.name} str() - expected Another Guitar (2016): $300.00. Got {another_guitar}.")


main()
