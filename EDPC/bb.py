import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,K = MI()
h = LI()
INF = float("inf")
dp = [INF] *(N)
dp[0] = 0
for i in range(N):
    for j in range(K+1):
        if i + j >= N:
            break
        dp[i+j] = min(dp[i+j], dp[i] + abs(h[i]-h[i+j]))
    
print(dp[-1])
