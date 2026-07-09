from math import sin

def f(a, b, c):
    A = 2 * a - b - sin(c)
    B = 5 + abs(c)
    return A / B

t, s = map(float, input().split())

f1 = f(t, -2 * s, 1.17)
f2 = f(2.2, t, s - t)

f3 = f1 + f2

print(f"{f3:.2f}")