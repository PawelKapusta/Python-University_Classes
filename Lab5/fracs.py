import math


def is_zer0(frac):
    return frac[0] == 0


def compute_lcm(x, y):
    return (x * y) // math.gcd(x, y)


def reduce_frac(x, y):
    d = math.gcd(x, y)
    return [x // d, y // d]


def add_frac(franc1, franc2):
    least = compute_lcm(franc1[1], franc2[1]);
    numerator = int(franc1[0] * (least / franc1[1]) + franc2[0] * (least / franc2[1]))
    return reduce_frac(numerator, least)


def sub_frac(franc1, franc2):
    least = compute_lcm(franc1[1], franc2[1]);
    numerator = int(franc1[0] * (least / franc1[1]) - franc2[0] * (least / franc2[1]))
    return reduce_frac(numerator, least)


def mul_frac(frac1, frac2):
    numerator = frac1[0] * frac2[0]
    dominator = frac1[1] * frac2[1]
    return reduce_frac(numerator, dominator)


def div_frac(frac1, frac2):
    numerator = frac1[0] * frac2[1]
    dominator = frac1[1] * frac2[0]
    return reduce_frac(numerator, dominator)


def is_positive(frac):
    return frac[0] > 0 and frac[1] > 0 or frac[0] < 0 and frac[1] < 0


def cmp_frac(frac1, frac2):
    dominator = compute_lcm(frac1[1], frac2[1])
    numerator1 = frac1[0] * (dominator / frac1[1])
    numerator2 = frac2[0] * (dominator / frac2[1])
    if numerator1 > numerator2:
        return 1
    elif numerator2 > numerator1:
        return -1
    else:
        return 0


def frac2float(frac):
    return [float(frac[0]), float(frac[1])]
