import math


def area(a, b, c):
  if not a + b >= c and a + c >= b and b + c >= a:
    raise ValueError('Not valid triangle check lengths of the sides')

  d = (a + b + c) / 2
  return math.sqrt(d * (d - a) * (d - b) * (d - c))


print("Area of triangle with a = 3, b = 4, c = 5 equals = ", area(3, 4, 5))
print("Area of triangle with a = 15, b = 4, c = 50 equals = ", area(15, 4, 50))
