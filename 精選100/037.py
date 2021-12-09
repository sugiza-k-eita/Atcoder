import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M = MI()
ns = LI()

dp = [[i for i in range(N+1)] for j in range(M)]

for i in range(M):
    for j in range(1,N+1):
        if ns[i] <= j:
            dp[i][j] = min(dp[i-1][j], dp[i][j-ns[i]]+1)
        else:
            dp[i][j] = dp[i-1][j]

# for j in dp:
#     print(j)
print(dp[-1][-1])