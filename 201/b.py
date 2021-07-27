n = int(input())
table = []
for i in range(n):
    s, t = input().split()
    t = int(t)
    table.append((t, s))

table.sort()
table.reverse()
print(table[1][1])
