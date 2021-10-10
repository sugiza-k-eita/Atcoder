N = int(input())
ns = list(map(int, input().split()))
dp = [10001]*N
dp[0] = 0
for i in range(1, N):
    if i == 1:
        dp[i] = abs(ns[i-1]-ns[i])
        continue
    dp[i] = min(abs(ns[i-1]-ns[i])+dp[i-1], abs(ns[i-2]-ns[i])+dp[i-2])
print(dp[-1])

N = int(input())
ns = list(map(int, input().split()))
dp = [10001]*N
dp[0] = 0
for i in range(2, N):
    dp[i] = min(abs(ns[i-1]-ns[i])+dp[i-1], abs(ns[i-2]-ns[i])+dp[i-2])
print(dp[-1])
