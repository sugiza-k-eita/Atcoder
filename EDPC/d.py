N, W = map(int, input().split())
dp = [[0]*(W+1) for i in range(N+1)]
"""
N番目のものを加味した時、Wgのおもちゃの最も価値の高い値を出す
"""
for i in range(1, N+1):
    w, v = map(int, input().split())
    for j in range(1, W+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(max(dp[-1]))
