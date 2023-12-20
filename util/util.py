from functools import reduce
from math import gcd


def simple_print(arr):
    string = ''
    for line in arr:
        string += ''.join([c for c in line])
        string += '\n'
    print(string)


def lcm(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)
