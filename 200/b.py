n, k = map(int, input().split())
for i in range(k):
    n = int(n)
    if n % 200 == 0:
        n = n/200
    else:
        n = str(n)
        n = n+"200"
    ans = int(n)

print(ans)
