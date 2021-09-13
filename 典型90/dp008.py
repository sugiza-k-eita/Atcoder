MOD = 10**9 + 7
N = int(input())
S = input()
S = "*"+S
t = "*atcoder"
dp = [[0 for i in range(len(t))] for j in range(len(S))]
dp[0][0] = 1
for i in range(1, len(S)):
    for j in range(len(t)):
        if S[i] == t[j]:
            dp[i][j] = int(dp[i-1][j-1] + dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# for i in dp:
#     print(i)

print(dp[-1][-1] % MOD)
