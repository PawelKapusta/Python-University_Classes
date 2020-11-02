def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        output = 1
        for element in range(2,n+1):
            output = output * element
    return output;


print(factorial(int(input("Write number to get factorial: "))))
