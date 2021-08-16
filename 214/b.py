S, T = map(int, input().split())
count = 0
for i in range(101):
    for j in range(101):
        for k in range(101):
            if i+j + k <= S and i*j*k <= T:
                count += 1
print(count)
