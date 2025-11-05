"""
CP1404 Practical 7
Project Management
Estimated completion time: 1.5 hours
Actual completion time:
"""
from project import Project
from datetime import datetime


def main():
    """Menu with options for project management"""
    MENU = ("- (L)oad projects \n- (S)ave projects \n- (D)isplay projects \n- (F)ilter projects by date \n"
            "- (A)dd new project \n- (U)pdate project \n- (Q)uit")
    print("Welcome to Pythonic Project Management")
    projects = load_projects()
    print(MENU)
    menu_choice = input(">>> ").upper()
    while menu_choice != "Q":
        if menu_choice == "L":
            filename = input("Enter project filename: ")
            projects = load_projects(filename)
        elif menu_choice == "S":
            filename = input("Enter project filename: ")
            save_projects(projects, filename)
        elif menu_choice == "D":
            display_projects(projects)
        elif menu_choice == "F":
            filter_projects(projects)
        elif menu_choice == "A":
            projects.append(add_new_project())
        elif menu_choice == "U":
            update_project(projects)
        else:
            print("Invalid menu choice")
        print(MENU)
        menu_choice = input(">>> ").upper()
    save_projects(projects)
    print("Thank you for using custom-built project management software.")


def load_projects(filename="projects.txt"):
    """Load projects from file"""
    projects = []
    try:
        with open(filename, "r") as in_file:
            in_file.readline()
            for line in in_file:
                parts = line.strip().split("\t")
                project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
                projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    return projects


def save_projects(projects, filename="projects.txt"):
    """Save projects to file."""
    with open(filename, "w") as out_file:
        print("Name	Start Date	Priority	Cost Estimate	Completion Percentage", file=out_file)
        for project in projects:
            print(f"{project.name}\t{project.start_date}\t{project.priority}\t{project.estimated_cost}\t"
                  f"{project.completion_percentage}", file=out_file)


def display_projects(projects):
    """Display two groups: incomplete projects; completed projects, both sorted by priority"""
    projects.sort()
    completed_projects = []
    incomplete_projects = []
    for project in projects:
        if project.is_complete():
            completed_projects.append(str(project))
        else:
            incomplete_projects.append(str(project))
    print("Incomplete Projects:")
    for project in incomplete_projects:
        print(project)
    print("Completed Projects:")
    for project in completed_projects:
        print(project)


def filter_projects(projects):
    """Ask the user for a date and display only projects that start after that date, sorted by date"""
    filter_date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    try:
        filter_date = datetime.strptime(filter_date_string, "%d/%m/%Y").date()
    except ValueError:
        print("Invalid date. Use dd/mm/yyyy.")
        return
    for project in projects:
        if project.start_date > filter_date:
            print(project)


def add_new_project():
    """Ask the user for the inputs and add a new project to memory"""
    print("Let's add a new project")
    name = input("Name: ")
    start_date = input("Start date (dd/mm/yyyy): ")
    priority = input("Priority: ")
    estimated_cost = input("Cost estimate: $")
    completion_percentage = input("Completion percentage: ")
    return Project(name, start_date, priority, estimated_cost, completion_percentage)


def update_project(projects):
    """Choose a project, then modify the completion % and/or priority"""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    project_choice = int(input("Project choice: "))
    print(projects[project_choice])
    new_percentage = int(input("New percentage: "))
    new_priority = input("New priority: ")
    projects[project_choice].completion_percentage = new_percentage
    projects[project_choice].priority = new_priority


main()
