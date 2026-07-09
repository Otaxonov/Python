from math import factorial

def t(x):
    n = 11

    s1 = 0
    for k in range(n):
        s1 += pow(x, 2 * k + 1) / factorial(2 * k + 1)

    s2 = 0
    for k in range(n):
        s2 += pow(x, 2 * k) / factorial(2 * k)

    return s1 / s2

y = float(input())

T = (1.7 * t(0.25) + 2 * t(1 + y)) / (6 - t(pow(y, 2) - 1))

print(f"{T:.2f}")