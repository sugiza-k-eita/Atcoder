"""
dp[i][j] = i番目までのお菓子で価値がちょうどvとなる選び方の重さの最小値
"""

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N, W = MI()
box = [[] for i in range(N)]
for i in range(N):
    w,v = MI()
    box[i] = [w,v]


INF = float("inf")
dp = [[INF]*(10**3+1) for i in range(N+1)]
dp[0][0] = 0

for i in range(N):
    v = box[i][1]
    w = box[i][0]
    dp[i][0] = 0
    for j in range(10**5):
        if j >= v:
            dp[i+1][j] = min(dp[i][j-v]+w, dp[i][j])

for i in range(N,-1,-1):
    if dp[-1][i] <= W:
        print(i)
        exit() 

