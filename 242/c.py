import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
dp  =  [[0]*9 for i in range(N)]
mod = 998244353

for j in range(9):
    dp[0][j] = 1

for i in range(1,N):
    for j in range(9):
        if j == 0:
            dp[i][0] += dp[i-1][0]+ dp[i-1][1]
        elif j == 8:
            dp[i][8] += dp[i-1][7]+ dp[i-1][8]
        else:
            dp[i][j] += dp[i-1][j-1]+ dp[i-1][j]+ dp[i-1][j+1]
        dp[i][j] %= mod

ans = sum(dp[-1])
print(ans%mod)


