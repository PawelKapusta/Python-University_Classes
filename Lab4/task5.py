def reverse_list_iterative(L, left, right):
    number = (right - left) // 2
    for element in range(number):
        temp = L[right]
        L[right] = L[left]
        L[left] = temp
        right -= 1
        left += 1
    return L

def reverse_list_recursive(L, left, right):
    if (left == right):
        return L
    temp = L[right]
    L[right] = L[left]
    L[left] = temp
    return reverse_list_recursive(L,left + 1 ,right -1)

L = list(range(1, 11))
print(L, "\nIterative: ")
print(reverse_list_iterative(L, 3, 7))
L2 = list(range(1, 11))
print("Recursive: ")
print(reverse_list_recursive(L2, 3, 7))
