from math import pi

r1, r2, r3 = map(int, input().split())

s1 = pi * pow(r1, 2)
s2 = pi * pow(r2, 2)
s3 = pi * pow(r3, 2)

print(f"{s1:.2f} {s2:.2f} {s3:.2f}")