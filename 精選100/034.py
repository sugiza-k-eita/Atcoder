import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


N = II()
dp = [1]*(N+1)
if N == 1 or N == 0:
    print(1)
    exit()
for i in range(2, N+1):
    dp[i] = dp[i-2] + dp[i-1]
print(dp[N])
