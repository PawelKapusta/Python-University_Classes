import random


def prepare_list(N, K):
  numbers_list = []
  for i in range(N):
    numbers_list.append(random.randint(0, K - 1))
  numbers_list.sort()
  return numbers_list


def binary_search_recursive(L, left, right, y):
  if right >= left:
    mid = left + (right - left) // 2
    if L[mid] == y:
      return mid
    if L[mid] > y:
      return binary_search_recursive(L, left, mid - 1, y)
    return binary_search_recursive(L, mid + 1, right, y)
  return -1


numbers = prepare_list(10, 100)
print("My numbers: \n", numbers)
searched_number = numbers[random.randint(0, len(numbers) - 1)]
print('Looking value:', searched_number)
print('Occurrence on index:', binary_search_recursive(numbers, 0, len(numbers), searched_number))
