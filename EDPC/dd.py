import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,W = MI()
box = [[] for i in range(N)]
for i in range(N):
    w,v = MI()
    box[i] = [w,v]

# for xx in box:
#     print(xx)

dp = [[0]*(W+1) for i in range(N)] 

for i in range(N):
    for j in range(W+1):
        if j < box[i][0]:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
        else:
            dp[i][j] = max(dp[i-1][j-1],dp[i-1][j-box[i][0]] + box[i][1])
# for xx in dp:
#     print(xx)
print(dp[-1][-1])