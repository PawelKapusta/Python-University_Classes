import time

definition = {
  (0, 0): 0.5,
  (0, 1): 1,
  (1, 0): 0
}


def rec(i, j):
  if i == 0 and j == 0:
    return definition.get((0, 0))
  if i == 0:
    return definition.get((0, 1))
  if j == 0:
    return definition.get((1, 0))
  else:
    return 0.5 * (rec(i - 1, j) + rec(i, j - 1))


def dp(i, j):
  if (i, j) in definition.keys():
    return definition.get((i, j))
  if i == 0:
    return definition.get((0, 1))
  if j == 0:
    return definition.get((1, 0))
  else:
    definition[(i, j)] = 0.5 * (dp(i - 1, j) + dp(i, j - 1))
    return definition.get((i, j))


start = time.time()
answer_rec = rec(10, 9)
end = time.time()
start2 = time.time()
answer_dp = dp(10, 9)
end2 = time.time()
print("In recursion value is", answer_rec, "and time equals:", end - start)
print("In dynamic programming value is", answer_dp, "and time equals:", end2 - start2)

