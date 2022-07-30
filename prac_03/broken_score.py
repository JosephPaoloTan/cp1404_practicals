"""
CP1404/CP5632 - Practical
Program to determine score status
"""

# TODO: Fix this!


def main():
    """Score status program"""
    score = float(input("Enter score: "))
    print(determine_score_status(score))


def determine_score_status(score):
    """Determine the status of the score"""
    if score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    elif score < 50:
        print("Bad")
    else:
        print("Invalid score")


main()
