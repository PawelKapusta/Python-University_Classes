def replace_char(word):
    return str(word).replace('.', '').replace(',', '')

line = "Python is a high-level programming language designed to be easy to read and simple to implement.\n" \
       "It is open source, which means it is free to use, even for commercial applications.\n" \
       "Python can run on Mac, Windows, and Unix systems and has also been ported to Java and .NET virtual machines."
words = line.split()
results = list(map(replace_char, words))
print("Length of characters in word line:",sum(len(x) for x in results))
