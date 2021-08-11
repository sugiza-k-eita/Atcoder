N = int(input())
dp = [[0]*3 for i in range(N+1)]

for i in range(1, N+1):
    a, b, c = map(int, input().split())
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + a
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + b
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + c

print(max(dp[-1]))
"""
i日目でaを選んだ場合の最大値は、i-1日目でB or C を選んだ場合の大きい値
"""
