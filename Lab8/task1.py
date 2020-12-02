def solve1(a, b, c):
  if a == 0:
    if b == 0:
      if c == 0:
        print("identity equation")
      else:
        print("No solutions")
    else:
      if c == 0:
        print("Solution: y = 0")
      else:
        print("Solution: y =", -c / b)
  else:
    if b == 0:
      if c == 0:
        print("Solution: x = 0")
      else:
        print("Solution: x =", -c / a)
    else:
      if c == 0:
        print("Solution: y =", -a / b, "* x")
      else:
        print("Solution: y =", -a / b, "* x +", -c / b)


print("Solution for equation 5x + 10y + 50 = 0: ")
solve1(5, 10, 50)
