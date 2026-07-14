# map(func, data), filter(condition(True), data)

data = [2, 6, 7, 89, 11, 100]

d1 = list(map(lambda a: a ** 2, data))
print(d1)

d2 = list(filter(lambda a: a % 2 == 0, data))
print(d2)