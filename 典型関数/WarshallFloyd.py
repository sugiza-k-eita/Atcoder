import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

V,E = MI()
INF = float("inf")
def WarshallFloyd(node,edge):
    min_dist = [[INF]*node for i in range(node)]
    for i in range(node):
        min_dist[i][i] = 0

    for i in range(edge):
        _from,_to,cost = MI()
        if min_dist[_from][_to] > cost:
            min_dist[_from][_to] = cost

    for mid in range(node):
        for start in range(node):
            if min_dist[start][mid] == INF:
                continue
            for goal in range(node):
                if min_dist[mid][goal] == INF:
                    continue
                if min_dist[start][goal] > min_dist[start][mid]+min_dist[mid][goal]:
                    min_dist[start][goal] = min_dist[start][mid]+min_dist[mid][goal]



    neg_FLG = False
    #負閉路探し
    for i in range(node):
        if min_dist[i][i] < 0:
            neg_FLG = True
            break

    return min_dist,neg_FLG

min_dist, negflg= WarshallFloyd(V,E)

if negflg:
    print("NEGATIVE CYCLE")
    exit()   


for i in range(V):
    for j in range(V):
        if min_dist[i][j] == INF:
            min_dist[i][j] = "INF"

for xx in min_dist:
    print(*xx, sep=" ")

