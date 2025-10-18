"""
CP1404/CP5632 - Practical_05
hex_colours
"""

NAME_TO_CODE = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc"
}

print(NAME_TO_CODE)

color_name = input("Color name: ").lower()
while color_name != "":
    try:
        print(NAME_TO_CODE[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Color name: ").lower()