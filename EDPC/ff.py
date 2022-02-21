"""
斜めにたどって答える
"""

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

s = S()
t = S()
s = "*"+s
t = "/"+t

s_leng = len(s)
t_leng= len(t)

dp = [[0]*(t_leng) for i in range(s_leng)]

for i in range(1,s_leng):
    for j in range(1,t_leng):
        if s[i] == t[j]:
            dp[i][j] = max(dp[i-1][j-1] + 1,dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])

ans = dp[-1][-1]
word = ''
s_leng -= 1
t_leng -= 1

while ans > 0:
    if dp[s_leng][t_leng] == dp[s_leng-1][t_leng]:
        s_leng -= 1
    elif dp[s_leng][t_leng] == dp[s_leng][t_leng-1]:
        t_leng -= 1      
    else:
        #斜めから来た場合は、
        word += s[s_leng]
        s_leng -= 1
        t_leng -= 1
        ans -= 1

print(word[::-1])


