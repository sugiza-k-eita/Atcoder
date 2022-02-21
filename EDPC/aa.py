import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
h = LI()
INF = float("inf")
dp = [INF] *(N)

dp[0] = 0
dp[1] = abs(h[0]-h[1])

for i in range(2,N):
    dp[i] = min(dp[i-2] + abs(h[i-2]-h[i]), dp[i-1] + abs(h[i-1]-h[i]))
# print(dp)
print(dp[-1])