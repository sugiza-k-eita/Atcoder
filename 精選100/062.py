import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

H,W = MI()
INF = float("inf")
tmp_dist = [[INF]*10 for i in range(10)]

for i in range(10):
    costs = LI()
    for j in range(len(costs)):
        tmp_dist[i][j] = costs[j]
walls = [[]for i in range(H)]
for h in range(H):
    wall = LI()
    walls[h] = wall


INF = float("inf")
def WarshallFloyd(node,tmp_dist):
    for mid in range(node):
        for start in range(node):
            if tmp_dist[start][mid] == INF:
                continue
            for goal in range(node):
                if tmp_dist[mid][goal] == INF:
                    continue
                if tmp_dist[start][goal] > tmp_dist[start][mid]+tmp_dist[mid][goal]:
                    tmp_dist[start][goal] = tmp_dist[start][mid]+tmp_dist[mid][goal]
    min_dist = tmp_dist

    neg_FLG = False
    #負閉路探し
    for i in range(node):
        if min_dist[i][i] < 0:
            neg_FLG = True
            break

    return min_dist,neg_FLG

tmp_min_dist, flg = WarshallFloyd(10,tmp_dist)
min_dist, flg = WarshallFloyd(10,tmp_min_dist)

ans = 0


for h in range(H):
    for w in range(W):
        wall = walls[h][w]
        if wall == -1:
            continue
        ans += min_dist[wall][1]
print(ans)