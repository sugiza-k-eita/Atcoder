import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M = MI()
INF = float("inf")
D = [0]
C = [0]

for i in range(N):
    a = II()
    D.append(a)
for j in range(M):
    b = II()
    C.append(b)

dp = [[INF] * (N+1) for _ in range(M+1)]
for x in range(0,M+1):
    dp[x][0] = 0
# print(D)
# print(C)

for i in range(1,M+1):
    for j in range(1,N+1):
        dp[i][j] = min(dp[i-1][j], dp[i-1][j-1]+C[i]*D[j])
#     print(dp[i])
# for xx in dp:
#     print(xx)
print(dp[-1][-1])