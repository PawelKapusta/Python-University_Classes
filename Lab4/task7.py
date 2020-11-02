returned = []

def flatten(seq):
    for item in seq:
        if isinstance(item, (list, tuple)):
            flatten(item)
        else:
            returned.append(item)
    return returned

seq = [1, (2, 3), [], [4, (5, 6, 7)], 8, [9]]
print(flatten(seq))
