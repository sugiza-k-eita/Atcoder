K = int(input())

if K %9 != 0:
    print(0)
    exit()

dp = [0]*(K+1)
dp[0] = 1
#dp[9] =1
mod = 10**9+7
for i in range(1,K+1):
    for j in range(1,10):
        dp[i] += dp[i-j]
    dp[i] %=mod
print(dp[-1])

