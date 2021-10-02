N = int(input())
ns = list(map(int, input().split()))
MOD = 998244353
dp = [[0]*10 for i in range(N+1)]

dp[0][ns[0]] = 1

for i in range(1, N):
    for j in range(10):
        F = (j+ns[i]) % 10
        G = (j*ns[i]) % 10
        dp[i][F] += dp[i-1][j]
        dp[i][G] += dp[i - 1][j]
        # ＝じゃなくて加算する理由としてはdp[i][F&G]が2以上のときに対応している
        dp[i][F] %= MOD
        dp[i][G] %= MOD
for i in range(10):
    print(dp[N-1][i])
