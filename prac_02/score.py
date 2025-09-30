"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    if score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    print(determine_grade(score))
    print(determine_grade(random.randint(1, 100)))


def determine_grade(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
