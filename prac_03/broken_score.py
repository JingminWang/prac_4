"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


# TODO: Fix this!
def main():
    score = float(input("Enter score: "))
    print(return_result(score))
    print()
    import random
    score_r = random.randint(1, 100)
    print(score_r)
    print(return_result(score_r))


def return_result(score):
    if score < 0 or score > 100:
        return ("Invalid score")
    elif score >= 90:
        return ("Excellent")
    elif score >= 50:
        return ("Passable")
    else:
        return ("Bad")


main()
