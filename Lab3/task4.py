while True:
    text = input("Write number that you want to power by 3 or \'stop\' if you want to end: ")
    if text == "stop":
        break
    else:
        try:
            number = float(text)
        except ValueError:
            print("This is not a number")
        else:
            print(number ** 3)
