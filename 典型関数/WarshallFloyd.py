import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

V,E = MI()
INF = float("inf")

tmp_dist = [[INF]*10 for i in range(10)]

for i in range(10):
    costs = LI()
    for j in range(len(costs)):
        tmp_dist[i][j] = costs[j]
walls = [[]for i in range(V)]

for h in range(V):
    wall = LI()
    walls[h] = wall


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

min_dist, negflg = WarshallFloyd(10,tmp_dist)

if negflg:
    print("NEGATIVE CYCLE")
    exit()   


for i in range(V):
    for j in range(V):
        if min_dist[i][j] == INF:
            min_dist[i][j] = "INF"

for xx in min_dist:
    print(*xx, sep=" ")

