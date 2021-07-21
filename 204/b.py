n = int(input())
ns = list(map(int, input().split()))
count = 0
for i in ns:
    while True:
        if i <= 10:
            break
        else:
            i -= 1
            count += 1

print(count)
