n, x = map(int, input().split())
ns = list(map(int, input().split()))
ans = []
for i in ns:
    if i != x:
        ans.append(i)

if len(ans) > 0:
    print(*ans, sep=" ")
else:
    print("")
