import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


N, W = MI()
box = [LI() for _ in [None]*(N)]

dp = [[0]*(W+1) for i in range(N+1)]

for i in range(1, N+1):
    v, w = box[i-1]
    for j in range(1, W+1):
        if j >= w:
            dp[i][j] = max(v+dp[i-1][j-w], dp[i-1][j])
        else:
            dp[i][j] = dp[i-1][j]

# for i in range(N+1):
#     print(dp[i])
print(dp[N][W])
