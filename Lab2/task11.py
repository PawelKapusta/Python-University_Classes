word = "word"
returned = ""
for letter in word:
    returned += letter + '_'
print(returned[:len(returned) - 1])