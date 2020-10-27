import roman
def roman2Int(string):
    romanValues = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
             'CD': 400, 'CM': 900}
    index = 0
    num = 0
    while index < len(string):
        if index + 1 < len(string) and string[index:index + 2] in romanValues:
            num += romanValues[string[index:index + 2]]
            index += 2
        else:
            num += romanValues[string[index]]
            index += 1
    return num


print("1 option:")
print(roman2Int("III"))
print(roman2Int("CDXLIII"))
print("2 option:")
print(roman.fromRoman("III"))
print(roman.fromRoman("CDXLIII"))
