# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
import copy
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

# O((N+M)logN)
from heapq import heappush, heappop
from collections import defaultdict
# 多重辺にも対応
# V=ノード数,E=エッジ数とすると、計算量はO((V+E)logV)
def Dijkstra(adj, start):
    # adjがstartと隣接するnode,startは出発点
    inf = 10**18
    MOD = 10**9+7
    n = len(adj)
    dist = [inf]*n
    prev = [inf]*n
    # prev[i]:頂点iに至る直前に居た頂点の番号．これを持っておけば，goalからstartまで戻れる
    dist[start] = 0
    hq = [(0, start)]
    while hq:
        d, u = heappop(hq)  # hpから最小値を取り出している
        # 最初は 0,startを取り出している
        # 0からstartまで最短経路を出すため
        if dist[u] < d:  # 既により最適な経路がある
            continue
        for v, cost in adj[u].items():  # u -cost-> v
            # 各要素のキーkeyと値valueの両方に対してforループ処理を行いたい場合は、items()メソッドを使う。
            if dist[v] == (dist[u] + cost):
                continue

            elif dist[v] > (dist[u] + cost):
                dist[v] = dist[u] + cost
                heappush(hq, (dist[v], v))  # hp に　dist[v]とvをpush(追加)している
                # hpに格納しているのは、移動コスト(dist[v])とその場所
                prev[v] = u  # prev[v](現在地)はuという場所からきたことを示している
    return dist
    #distはスタートからの各nodeまでの最小コストを出力
    #varietyは最小コストで行く方法は何通りあるかを出力

mod = 10**9+7
N,M = MI()
dd = {}
inf = 10**18
G = [defaultdict(int) for i in range(N)]
index = []
for m in range(M):
    a,b,c = MI()
    a -= 1
    b -= 1
    G[a][b] = c
    G[b][a] = c
    index.append([a,b,c])
odist = []
for i in range(N):
    dist  = Dijkstra(G,i)
    odist.append(dist)

ans = 0
for m in range(M):
    tmp = 0
    s,t,c = index[m][0],index[m][1],index[m][2]
    nG = copy.deepcopy(G)
    nG[s].pop(t)
    nG[t].pop(s)
    for i in range(N):
        dist = Dijkstra(nG,i)
        if odist[i] == dist:
            ans += 1
print(ans)



