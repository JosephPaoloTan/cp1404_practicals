from guitar import Guitar
CURRENT_YEAR = 2022


def main():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = Guitar(name, year, cost)
    other = Guitar("another guitar", 2013)
    print(guitar)
    print(other)
    print(f"{guitar.name} get_age() - Expected {100}, got {guitar.get_age()}")
    print(f"{other.name} get_age() - Expected {9}, got {other.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected {True}, got {guitar.is_vintage()}")
    print(f"{other.name} is_vintage - Expected {False}, got {other.is_vintage()}")


main()
