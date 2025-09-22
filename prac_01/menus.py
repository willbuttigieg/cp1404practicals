"""
CP1404
Menus

Pseudocode:
get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message
"""

MENU = "(H)ello \n(G)oodbye \n(Q)uit \n>>> "

name = input("Enter name: ")
menu_choice = input(MENU).upper()
while menu_choice != "Q":
    if menu_choice == "H":
        print(f"Hello {name}")
    elif menu_choice == "G":
        print(f"Goodbye {name}")
    else:
        print(f"Invalid choice")
    menu_choice = input(MENU).upper()
print("Finished.")

