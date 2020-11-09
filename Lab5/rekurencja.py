def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        output = 1
        for element in range(2,n+1):
            output = output * element
    return output;

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        previous_number = 1; output = 1
        for element in range(2,n):
            previous_previous_number = output
            output +=  previous_number
            previous_number = previous_previous_number
        return output