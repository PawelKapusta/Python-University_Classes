import random


def prepare_list(N, K):
    numbers_list = []
    for i in range(N):
        numbers_list.append(random.randint(0, K - 1))
    return numbers_list


def linear_search(elements, search):
    occurrences = []
    for i in range(len(elements)):
        if elements[i] == search:
            occurrences.append(i)
    return occurrences


numbers = prepare_list(100, 10)
print("My numbers: \n",numbers)
searched_number = numbers[random.randint(0, len(numbers) - 1)]
print('Looking value:', searched_number)
indexes_list = linear_search(numbers, searched_number)
print("Number of occurrences value",searched_number,"equals:", len(indexes_list))
print('Occurrence on index:',indexes_list)
