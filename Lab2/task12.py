import re
line = "Python is a high-level programming language designed to be easy to read and simple to implement.\n" \
       "It is open source, which means it is free to use, even for commercial applications.\n" \
       "Python can run on Mac, Windows, and Unix systems and has also been ported to Java and .NET virtual machines."
words = re.split(".,")
first = ""
last = ""
for l in words:
    first += l[0]
    last += l[len(l)-1]
print("Word with first letters of each words in line", first)
print("Word with last letters of each words in line", last)