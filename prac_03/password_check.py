"""Program that gets password and prints asterisks based on the number of characters"""

MINIMUM_LENGTH = 5


def main():
    """Get password and print asterisks."""
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def get_password(minimum_length):
    """Obtain password and check length."""
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Invalid password")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisks(characters):
    """Print asterisks based on number of characters"""
    print("*" * len(characters))


main()
