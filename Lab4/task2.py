def measure(length):
    output = "| "
    sectionToAdd = ". . . . | "
    try:
        length = int(length)
    except ValueError:
        return "It is not correct number in example of task 3.5"
    else:
        for digit in range(length):
            output += sectionToAdd
        output += "\n0"
        for digit in range(length):
            nextValue = ''.ljust(len(sectionToAdd) - len(str(digit + 1)), ' ') \
                        + str(digit + 1)
            output += nextValue
        return output
def rectangle(first,second):
    output = ""
    try:
        firstSide = int(first)
        secondSide = int(second)
    except ValueError:
       return "Check your input, maybe you do not write a number"
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
    return output


print("Task 3.5:")
print(measure(input("Write length of measure as Integer: ")))
print("Task 3.6:")
print(rectangle(input("Write first side of rectangle: "),input("Write second side of rectangle: ")))


