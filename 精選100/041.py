import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

D,N= MI()
temperature = []
for _ in range(D):
    T = II()
    temperature.append(T)

lower_upper = [[] for i in range(N)]
charm = []
for i in range(N):
    A,B,C = MI()
    lower_upper[i].append(A)
    lower_upper[i].append(B)
    charm.append(C)

dp = [[-1]*N for i in range(D)]
for j in range(N):
    if temperature[0] < lower_upper[j][0] or temperature[0] > lower_upper[j][1]:
        continue
    dp[0][j] = charm[j]
for j in range(N):
    if temperature[1] < lower_upper[j][0] or temperature[1] > lower_upper[j][1]:
        continue
    for k in range(N):
        if dp[0][k] == -1:
            continue
        dp[1][j] = max(dp[1][j], abs(charm[k]-charm[j]))



for i in range(2,D):
    for j in range(N):
        if temperature[i] < lower_upper[j][0] or temperature[i] > lower_upper[j][1]:
            continue
        for k in range(N):
            if dp[i-1][k] == -1:
                continue
            dp[i][j] = max(dp[i][j], dp[i-1][k]+abs(charm[k]-charm[j]))

# for xx in dp:
#     print(xx)     

print(max(dp[-1]))