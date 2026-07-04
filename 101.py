n = int(input())
m = list(map(int, input().split()))

avg = sum(m) / n

l = []
for i in range(n):
    if m[i] < avg:
        l.append(m[i])

a = sum(l) / len(l)
print(f"{a:.2f}")