from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

H,W = MI()


INF = float("inf")
tmp_dist = [[] for i in range(10)]
for i in range(10):
    tmp_dist[i] = LI()

walls = [[] for i in range(H)]
for i in range(H):
    walls[i] = LI()


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

min_dist,neg_flg = WarshallFloyd(10,tmp_dist)

# for xx in min_dist:
#     print(xx)


ans = 0
for h in range(H):
    for w in range(W):
        if walls[h][w] == -1:
            continue
        else:
            ans += min_dist[walls[h][w]][1]
print(ans)