import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

H,W = MI()
inf = float("INF")
box = [[None]*W for i in range(H)]
dp = [[inf]*W for i in range(H)]
for i in range(H):
    ns = S()
    for j in range(W):
        box[i][j] = ns[j]

if box[0][0] == ".":
    dp[0][0] = 0
else:
    dp[0][0] = 1


for h in range(1,H):
    if box[h][0] == box[h-1][0]:
        dp[h][0] = dp[h-1][0]
    else:
        dp[h][0] = dp[h-1][0] + 1

for w in range(1,W):
    if box[0][w] ==box[0][w-1]:
        dp[0][w] = dp[0][w-1]
    else:
        dp[0][w] = dp[0][w-1] + 1


for h in range(1,H):
    for w in range(1,W):
        if box[h][w] == box[h-1][w]:
            dp[h][w] = dp[h-1][w]
        else:
            dp[h][w] = dp[h-1][w]+1

        if box[h][w] == box[h][w-1]:
            dp[h][w] = min(dp[h][w-1],dp[h][w])
        else:
            dp[h][w] = min(dp[h][w-1]+1,dp[h][w])

# for xx in dp:
#     print(xx)
if box[-1][-1] == "#":
    dp[-1][-1] += 1

print(dp[-1][-1]//2)