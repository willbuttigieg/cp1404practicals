"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_data = load_subject_data(FILENAME)
    display_subject_data(subject_data)
    # print(subject_data)


def load_subject_data(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    all_parts = []
    input_file = open(filename)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("----------")
        all_parts.append(parts)
    input_file.close()
    return all_parts


def display_subject_data(subject_data):
    """Display formatted subject data."""
    for part in subject_data:
        print(f"{part[0]} is taught by {part[1]:<12} and has {part[2]:3} students")


main()
