n, k = map(int, input().split())
ns = list(map(int, input().split()))
table1 = []
dict = {}
for i in range(n):
    table1.append(ns[i])

ns.sort()
standard = k//n
tmp = k % n

for i in range(n):
    dict[ns[i]] = standard
if tmp > 0:
    for i in range(tmp):
        dict[ns[i]] += 1
for i in table1:
    print(dict[i])
