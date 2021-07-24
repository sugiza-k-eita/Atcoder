n = int(input())
ns = list(map(int, input().split()))
ns.sort()
flg = 0
if len(ns) == 1 and ns[0] != 1:
    flg = 1

for i in range(n-1):
    if ns[i] + 1 == ns[i+1]:
        continue
    else:
        flg = 1
if flg == 1:
    print("No")
else:
    print("Yes")
