from silver_service_taxi import SilverServiceTaxi
from taxi import Taxi


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None
    total_fare = 0
    print("Lets drive!")
    print("q)uit, c)hoose taxi, d)rive")
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            current_taxi = choose_taxi(current_taxi, taxis)
            print(f"Bill to date: ${total_fare:.2f}")
        elif menu_choice == "d":
            fare = drive_taxi(current_taxi)
            total_fare += fare
            print(f"Bill to date: ${total_fare:.2f}")
        else:
            print("Invalid option")
        print("q)uit, c)hoose taxi, d)rive")
        menu_choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_fare:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(current_taxi, taxis):
    """Choose a taxi."""
    taxi = current_taxi
    print("Taxis available:")
    display_taxis(taxis)
    choice = int(input("Choose taxi: "))
    if choice in range(len(taxis)):
        taxi = taxis[choice]
    else:
        print("Invalid taxi choice")
    return taxi


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def drive_taxi(current_taxi):
    """Drive the chosen taxi."""
    if current_taxi is None:
        print("You need to choose a taxi before you can drive")
        return 0
    distance = int(input("Drive how far? "))
    current_taxi.drive(distance)
    fare = current_taxi.get_fare()
    print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
    return fare


main()
