import random

LINE_NUMBERS = 6
MINIMUM = 1
MAXIMUM = 45


def main():
    """Quick Picks Program"""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number of picks!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for i in range(number_of_quick_picks):
        quick_picks = []
        for j in range(LINE_NUMBERS):
            number = random.randint(MINIMUM, MAXIMUM)
            while number in quick_picks:
                number = random.randint(MINIMUM, MAXIMUM)
            quick_picks.append(number)
        quick_picks.sort()

        print(" ".join("{:2}".format(number) for number in quick_picks))


main()
