n = int(input())

start = pow(10, n - 1)
end = pow(10, n) - 1

for i in range(start, end):
    s = str(i)
    if '0' not in s:
        pass