#!/usr/bin/python3

def pow(a, b):
    result = 1
    if b < 0:
        a = 1 / a
        b = -b
    while b > 0:
        if b % 2 == 1:
            result *= a
        a *= a
        b //= 2
    return result

print(pow(2, 2))
print(pow(98, 2))
print(pow(98, 0))
print(pow(100, -2))
print(pow(-4, 5))
