import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
enjoy = [[] for i in range(N)]

for i in range(N):
    enjoy[i] = LI()

dp = [[0]*3 for i in range(N)]
for i in range(3):
    dp[0][i] += enjoy[0][i]

for i in range(1,N):
    for j in range(3):
        #今日
        for k in range(3):
            #昨日
            if j == k:
                continue
            dp[i][j] = max(dp[i-1][k] + enjoy[i][j],dp[i][j])

# for xx in dp:
#     print(xx)
print(max(dp[-1]))