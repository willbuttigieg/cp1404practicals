"""
display menu
get choice
while choice != <quit option>
    if choice == <first option>
        <do first task>
    else if choice == <second option>
        <do second task>
    ...
    else if choice == <n-th option>
        <do n-th task>
    else
        display invalid input error message
    display menu
    get choice
<do final thing, if needed>

Menu
(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit

Pseudocode:
function main
    function get_valid_score
    print menu
    get choice
    while choice != Q
        if choice == G
            function get_valid_score
        else if choice == P
            function print_result
        else if choice == S
            function show_stars
        else
            display invalid error message
        print menu
        get choice
    print farewell

function get_valid_score
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        display error message
        score = float(input("Enter score: "))
    return score

function print_result
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

function show_stars
    print("*" * score)

"""


def main():
    menu = """(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit"""
    score = get_valid_score()
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell")


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = int(input("Enter score: "))
    return score


def print_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


def show_stars(score):
    print("*" * score)


main()
