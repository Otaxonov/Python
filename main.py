from math import log

a, b, c, d = map(int, input().split())

s = 0
for m in range(1, a + 1):
    A = 3 * pow(m, 3) + 4 * m + 5
    B = pow(m, 3) + log(m)
    s += A / B

p = 1
for k in range(1, b + 1):
    p *= k / (pow(k, 3) + 7 * k + 5)

# Nested for loop
sp = 0
for i in range(1, c + 1):
    p1 = 1
    for m in range(1, d + 1):
        p1 *= (log(i) + pow(m, i)) / pow(m, i)
    sp += p1

print(f"{s:.2f} {p:.2f} {sp:.2f}")