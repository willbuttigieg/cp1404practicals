"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""


def convert_celcius_to_farenheit():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def convert_farenheit_to_celcius():
    fahrenheit = float(input("Fahrenheit : "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_celcius_to_farenheit()
        elif choice == "F":
            convert_farenheit_to_celcius()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


main()
