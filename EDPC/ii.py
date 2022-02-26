import sys
def LI(): return list(map(float,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

"""
i番目までにj回表が出たときの確率を考える
その後、N//2回以上の確率のみ思考
"""
N = II()
ns = LI()
ns = [0] + ns

dp = [[0]*(N+1) for i in range(N+1)]
dp[0][0] = 1
for i in range(1,N+1):
    for j in range(N+1):
        dp[i][j] = dp[i-1][j-1]*ns[i] 
        dp[i][j] += dp[i-1][j]*(1-ns[i])

if N %2 == 0:
    s = N//2
else:
    s = N//2 + 1
ans = 0
for j in range(s,N+1):
    ans += dp[-1][j]
print(ans)