n = int(input())
i = 0
while True:
    if n <= 0:
        days = i
        break
    else:
        i += 1
        n = n - i

print(days)
