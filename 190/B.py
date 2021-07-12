n, s, d = map(int, input().split())
table = []
for i in range(n):
    x, y = map(int, input().split())
    table.append([x, y])
count = 0
for i in range(n):
    if table[i][0] < s:
        if table[i][1] > d:
            count = 1

if count == 1:
    print("Yes")
else:
    print("No")
