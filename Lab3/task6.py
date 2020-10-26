output = ""
try:
    firstSide = int(input("Write first side of rectangle: "))
    secondSide = int(input("Write second side of rectangle: "))
except ValueError:
    print("Check your input, maybe you do not write a number")
else:
    for index in range(2 * firstSide + 1):
        if index % 2 == 0:
            output += "+"
            for i in range(secondSide):
                output += "---+"
            output += "\n"
        else:
            output += "|"
            for j in range(secondSide):
                output += "   |"
            output += "\n"
print(output)
