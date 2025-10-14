"""
CP1404 Practical
Emails
Estimate: 30 minutes
Actual:   32 minutes
"""


def main():
    """Get emails and store them with corresponding names"""
    name_to_email = {}
    email = input("Email: ")
    while email != "":
        possible_name = extract_name(email)
        name = check_name(possible_name)
        name_to_email[name] = email
        email = input("Email: ")
    print()
    for name, email in name_to_email.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract possible name from email"""
    name = email.split("@")[0].replace(".", " ").title()
    return name


def check_name(possible_name):
    """Check that extracted name is correct"""
    check = input(f"Is your name {possible_name}? (Y/n) ").lower()
    if check == "" or check == "y":
        return possible_name
    else:
        name = input("Name: ")
        return name


main()
