n = int(input())
n += 1
count = 1
while True:
    if n % 100 == 0:
        break
    else:
        n += 1
        count += 1

print(count)
