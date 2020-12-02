import random
random.seed()
n = int(input('Write n = '))
k = 0
for j in range(n):
    x = random.random()
    y = random.random()
    if x ** 2 + y ** 2 <= 1:
        k += 1
answer = 4 * k / n
print("Result pi =", answer)