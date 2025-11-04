"""
CP1404 Practical 7
Project Management
Estimated completion time: 1 hour
Actual completion time:
"""


def main():
    """Menu with options for project management"""
    MENU = ("- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date \n"
            "- (A)dd new project \n- (U)pdate project \n- (Q)uit")
    print(MENU)
    menu_choice = input(">>> ")
    while menu_choice != "Q":
        if menu_choice == "L":
            load_projects()
        elif menu_choice == "S":
            save_projects()
        elif menu_choice == "D":
            display_projects()
        elif menu_choice == "F":
            filter_projects()
        elif menu_choice == "A":
            add_new_project()
        elif menu_choice == "U":
            update_project()
        else:
            print("Invalid menu choice")
        print(MENU)
        menu_choice = input(">>> ")
    print("Thank you for using custom-built project management software.")


def load_projects():
    """Prompt the user for a filename to load projects from and load them"""


def save_projects():
    """Prompt the user for a filename to save projects to and save them"""


def display_projects():
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""


def filter_projects():
    """Ask the user for a date and display only projects that start after that date, sorted by date"""


def add_new_project():
    """Ask the user for the inputs and add a new project to memory"""


def update_project():
    """Choose a project, then modify the completion % and/or priority"""


main()
