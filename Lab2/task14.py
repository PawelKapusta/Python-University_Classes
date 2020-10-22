def replaceChar(word):
    return str(word).replace('.', '').replace(',', '')
def theLongest(words):
    return max(words,key=len)

line = "Python is a high-level programming language designed to be easy to read and simple to implement.\n" \
       "It is open source, which means it is free to use, even for commercial applications.\n" \
       "Python can run on Mac, Windows, and Unix systems and has also been ported to Java and .NET virtual machines."
words = line.split()
results = list(map(replaceChar, words))
long = theLongest(results)
print("The longest string in line is:",long,"and its length equals:",len(long))