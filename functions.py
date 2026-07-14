# Recursion Function
def countdown(n):
    if n <= 0:
        print('Time is Up!')
    else:
        countdown(n - 1)

countdown(5)

# 1. n = 5, 5 <= 0, countdown(n - 1)
# 2. n = 4, 4 <= 0, countdown(n - 1)
# 3. n = 3, 3 <= 0, countdown(n - 1)
# 4. n = 2, 2 <= 0, countdown(n - 1)
# 5. n = 1, 1 <= 0, countdown(n - 1)
# 6. n = 0, 0 <= 0, print('Time is Up!')