N, K = map(int, input().split())
ns = list(map(int, input().split()))
maximun = float("inf")
dp = [maximun]*N
dp[0] = 0
dp[1] = abs(ns[1]-ns[0])
for i in range(1, N):
    for j in range(max(0, i-K), i):
        dp[i] = min(abs(ns[i]-ns[j])+dp[j], dp[i])
print(dp[-1])
"pypyのみAC"
