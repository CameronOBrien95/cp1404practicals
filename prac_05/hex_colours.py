"""
CP1404/CP5632 Practical
Hexadecimal colour lookup
"""
COLOUR_TO_HEX_CODE = {"DARKORCHID": "#9932cc", "DEEPPINK": "#ff1493", "DODGERBLUE": "1e90ff", "FORESTGREEN": "#228b22",
                      "INDIANRED": "#cd5c5c", "LAVENDER": "#e6e6fa", "MAGENTA": "	#ff00ff", "MEDIUMBLUE": "#0000cd",
                      "MINTCREAM": "#f5fffa", "ORANGE": "#ffa500"}
colour = input("Enter a colour: ").upper()
while colour != "":
    if colour in COLOUR_TO_HEX_CODE:
        print(colour, "is", COLOUR_TO_HEX_CODE[colour])
    else:
        print("Invalid colour")
    colour = input("Enter a colour: ").upper()

