def daraja(n):
    for i in n:
        yield i ** 2

numbers = [1, 2, 3, 4, 5, 6]

kvadrat = daraja(numbers)

print(next(kvadrat))
print(next(kvadrat))
print(next(kvadrat))