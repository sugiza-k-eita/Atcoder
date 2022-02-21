"""
bfsを使って距離を測る
その際、距離の図り方は、dp[v] max(dp[u]+1,dp[v])で求める

"""

from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M = MI()

node = [[] for i in range(N)]
dp = [0]*N
for i in range(M):
    x,y = MI()
    x -= 1
    y -= 1
    node[x].append(y)

def dfs(u):
    if dp[u] 