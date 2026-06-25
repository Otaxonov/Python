# 046. Tarmoqlanuvchi 16.

x = float(input())

y = 0
if x > 2:
    y = 4
elif x < -1:
    y = 1 / pow(x, 2)
else:
    y = pow(x, 2)

print(f"{y:.2f}")