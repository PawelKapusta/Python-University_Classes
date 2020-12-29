import random


def random_numbers(N):
  numbers = prepare_int_numbers(N)
  random.shuffle(numbers)
  return numbers


def almost_sorted_numbers(N):
  numbers = prepare_int_numbers(N)
  for i in range(1, N):
    j = random.randint(i - 1, i)
    numbers[i], numbers[j] = numbers[j], numbers[i]
  return numbers


def almost_sorted_reversed_numbers(N):
  numbers = almost_sorted_numbers(N)
  numbers.reverse()
  return numbers


def prepare_int_numbers(N):
  numbers = []
  for i in range(0, N):
    numbers.append(i)
  return numbers


def gaussian_numbers(N):
  numbers = []
  for i in range(N):
    numbers.append(random.gauss(0, 1))
  return numbers


def repeating_numbers(N):
  numbers = []
  for i in range(N):
    numbers.append(random.randint(0, N // 2))
  random.shuffle(numbers)
  return numbers
