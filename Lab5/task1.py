import importlib
from Lab5 import rekurencja
import Lab5.rekurencja as rek
from Lab5.rekurencja import *
from Lab5.rekurencja import factorial
from Lab5.rekurencja import fibonacci as fib
print("1. rekurencja:")
print(rekurencja.factorial(6))
print(rekurencja.fibonacci(5))
print("--------\n2. rek:")
print(rek.factorial(6))
print(rek.fibonacci(5))
print("--------\n3. *:")
print(factorial(6))
print(fibonacci(5))
print("--------\n4. fib:")
print(fib(5))

importlib.reload(rekurencja)