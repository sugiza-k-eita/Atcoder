n = int(input())
min_a = 100000
min_b = 100000
table = []
ans = 200000
for i in range(n):
    a, b = map(int, input().split())
    table.append([a, b])

for i in range(n):
    for j in range(n):
        ans = min(ans, table[i][0]+table[j][1] if i ==
                  j else max(table[i][0], table[j][1]))

print(ans)
