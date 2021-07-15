n, x = map(int, input().split())
ns = list(map(int, input().split()))
even = []
for i in range(n):
    if i % 2 == 1:
        tmp = ns[i]-1
        even.append(tmp)
    else:
        even.append(ns[i])
acount = sum(even)

if acount <= x:
    print("Yes")
else:
    print("No")
