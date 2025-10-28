"""
CP1404 Practical
Hex Colours Program
"""

colour_to_code = {"absolute zero": "#0048BA", "amber": "#ffbf00", "aqua": "#00ffff", "apricot": "#fbceb1",
                  "asparagus": "#87a96b", "beige": "#f5f5dc", "bistre": "#3d2b1f", "black": "#000000",
                  "blond": "#faf0be", "chamoisee": "#a0785a"}

colour_name = input("Enter colour name: ").lower()
while colour_name != "":
    try:
        colour_code = colour_to_code[colour_name]
        print(colour_code)
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").lower()
