import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
H,W = MI()
box = [[] for i in range(H)]
go = [[0,1],[1,0]]
for i in range(H):
    box[i] = S()

dp = [[0]*W for i in range(H)]
dp[0][0] = 1
for i in range(1,H):
    if box[i][0] == "#":
        dp[i][0] = 0
    else:
        dp[i][0] += dp[i-1][0]

for j in range(1,W):
    if box[0][j] == "#":
        dp[0][j] = 0
    else:
        dp[0][j] += dp[0][j-1]

for i in range(1,H):
    for j in range(1,W):
        if box[i][j] == "#":
            continue
        dp[i][j] += dp[i-1][j] + dp[i][j-1]
        dp[i][j] %= 10**9+7

# for xx in dp:
#     print(xx)
print(dp[-1][-1])
