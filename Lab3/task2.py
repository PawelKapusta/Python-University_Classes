# 1)
L = [3, 5, 4]; L = L.sort()
# The sort() function does not return any value so it is not compiling as we want.
# Correct implementation:"
L = [3, 5, 4]
L = sorted(L)
print(L)

# 2)
x, y = 1, 2, 3
# As we know Tuple is a collection of objects wchich are ordered and immutable. So if we have
# two elements we could only have two values not more.
# Correct:
x, y, z = 1, 2, 3;

# 3)
X = 1, 2, 3; X[1] = 4
# As in before explanation we can not change value of Tuple, we can only create it again like:
X = 1, 2, 3
X = X[0], 4, X[1]

# 4)
X = [1, 2, 3]; X[3] = 4
# It is simply error, we are trying to assign value on index which is out of range.
# if we want to change the last element in array our index equals to len(X) - 1
#Correct:
X = [1,2,3]
X[len(X)  - 1] = 4

#5)
X = "abc" ; X.append("d")
# 'str' object has no attribute 'append'
#Correct:
X = "abc"
X += "d"

#6)
L = list(map(pow, range(8)))