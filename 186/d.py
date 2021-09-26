N = int(input())
ns = list(map(int, input().split()))
ns.sort()
# print(ns)
tmp = 0
ans = 0
for i in range(N):
    ans += ns[i]*i
    tmp += ns[i]*(N-i-1)
print(ans-tmp)
