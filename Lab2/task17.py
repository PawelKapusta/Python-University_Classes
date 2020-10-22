def replace_char(word):
    return str(word).replace('.','').replace(',','')

line = "Python is a high-level programming language designed to be easy to read and simple to implement.\n" \
       "It is open source, which means it is free to use, even for commercial applications.\n" \
       "Python can run on Mac, Windows, and Unix systems and has also been ported to Java and .NET virtual machines."
words = line.split()
results = list(map(replace_char,words))
for i in range(len(results)):
    results[i] = results[i].lower()
print("Sorted words with alphabet:",sorted(results))
print("Sorted words with length:",sorted(results,key = len))