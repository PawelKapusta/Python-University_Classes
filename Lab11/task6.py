from Lab11.task1 import *
import time


# If you want to print the lists that I am using in this program you have to uncomment print functions and also change number of numbers to sort
def partition(numbers, start, end):
  mid = start + (end - start) // 2
  pivot = numbers[mid]

  while start <= end:
    while numbers[start] < pivot:
      start += 1
    while numbers[end] > pivot:
      end -= 1
    if start <= end:
      numbers[start], numbers[end] = numbers[end], numbers[start]
      start += 1
      end -= 1
  return start


def iterative_quicksort(numbers):
  start = 0
  end = len(numbers) - 1
  stack = [start, end]

  while len(stack) > 0:
    end = stack.pop()
    start = stack.pop()

    pivot_index = partition(numbers, start, end)

    if pivot_index - 1 > start:
      stack.append(start)
      stack.append(pivot_index - 1)

    if pivot_index < end:
      stack.append(pivot_index)
      stack.append(end)


print('random numbers:')
numbers_list = random_numbers(100000)
# print(numbers_list)
start = time.time()
iterative_quicksort(numbers_list)
end = time.time()
# print(numbers_list)
print("Time: ", end - start, '\n')

print('almost sorted numbers:')
numbers_list = almost_sorted_numbers(100000)
# print(numbers_list)
start2 = time.time()
iterative_quicksort(numbers_list)
end2 = time.time()
# print(numbers_list)
print("Time: ", end2 - start2, '\n')

print('almost sorted reversed numbers:')
numbers_list = almost_sorted_reversed_numbers(100000)
# print(numbers_list)
start3 = time.time()
iterative_quicksort(numbers_list)
end3 = time.time()
# print(numbers_list)
print("Time: ", end3 - start3, '\n')

print('repeating numbers:')
numbers_list = repeating_numbers(100000)
# print(numbers_list)
start4 = time.time()
iterative_quicksort(numbers_list)
end4 = time.time()
# print(numbers_list,)
print("Time: ", end4 - start4, '\n')

print('gaussian numbers:')
numbers_list = gaussian_numbers(100000)
# print(numbers_list)
start5 = time.time()
iterative_quicksort(numbers_list)
end5 = time.time()
# print(numbers_list,)
print("Time: ", end5 - start5, '\n')
