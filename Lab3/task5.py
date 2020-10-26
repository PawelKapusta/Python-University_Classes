output = "| "
sectionToAdd = ". . . . | "
number = input("Write length of measure as Integer: ")
try:
    number = int(number)
except ValueError:
    print("This is not correct number")
else:
    for digit in range(number):
       output += sectionToAdd
    output += "\n0"
    for digit in range(number):
        nextValue = ''.ljust(len(sectionToAdd) - len(str(digit + 1)), ' ') \
                    + str(digit + 1)
        output += nextValue
    print(output)
