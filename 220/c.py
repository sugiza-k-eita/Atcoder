N = int(input())
ns = list(map(int, input().split()))
X = int(input())
ans = 0
tmp = sum(ns)

Int = X//tmp
ans += (Int)*N
Float = X % tmp
for i in range(N):
    Float = Float - ns[i]
    if Float < 0:
        break
    ans += 1
print(ans+1)
