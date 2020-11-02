def sum_seq(given_sequence):
    returned_sum = 0
    for element in given_sequence:
        if isinstance(element,(list,tuple)):
            returned_sum += sum_seq(element)
        else:
            returned_sum += element
    return returned_sum

given_sequence = [1,(2,3),[],[4,(5,6,7)],8,[9]]
print("Output: ", sum_seq(given_sequence))