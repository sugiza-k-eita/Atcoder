import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


N, W = MI()
box = [LI() for _ in [None]*(N)]

dp = [0]*(W+1)

for i in range(1, N+1):
    v, w = box[i-1]
    for j in range(w, W+1):
        dp[j] = max(v+dp[j-w], dp[j])


# for i in range(N+1):
#     print(dp[i])

print(dp[W])
