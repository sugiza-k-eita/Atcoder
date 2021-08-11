s = list(str(input()))
t = list(str(input()))

dp = [[0 for i in range(len(t)+1)] for j in range(len(s)+1)]

for i in range(len(s)):
    for j in range(len(t)):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j]+1
            # ↓なんでこれじゃだめなのかよくわからない。加算の方法がsによってではないのが良くないのかもしれない
            #dp[i+1][j+1] = max(dp[i+1][j]+1, dp[i][j+1])

        else:
            dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
"""
for x in range(len(s)+1):
    print(dp[x])
"""
ans = dp[-1][-1]
word = ''
p = len(s)
q = len(t)

while ans > 0:
    if dp[p][q] == dp[p-1][q]:
        p -= 1
    elif dp[p][q] == dp[p][q-1]:
        q -= 1
    else:
        p -= 1
        q -= 1
        ans -= 1
        word += t[q]
print(word[::-1])
