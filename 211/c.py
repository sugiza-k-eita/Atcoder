letter = "*chokudai"
leng = len(letter)
S = str(input())
S = "*"+S
MOD = 10 ** 9 + 7
dp = [[0]*leng for i in range(len(S))]
dp[0][0] = 1
for i in range(1, len(S)):
    for j in range(len(letter)):
        if S[i] == letter[j]:
            dp[i][j] = dp[i-1][j-1]+dp[i-1][j]
            dp[i][j] %= MOD
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])

# 一致したときはdp[i-1][j-1]+dp[i-1][j]
