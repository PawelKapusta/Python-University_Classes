import random

l1 = [random.randint(1,100) for i in range(25)]
l2 = [random.randint(1,100) for j in range(15)]
print("Our first list:",l1)
print("Our second lsit:",l2)
theSame = set(l1)
intersection = theSame.intersection(l2)
print("A)\n",list(intersection))
allNumbers = set(l1).union(l2)
print("B)\n",list(allNumbers))
