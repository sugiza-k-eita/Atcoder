import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

# 第13問:水diff O((N+M)logN)
from heapq import heappush, heappop
# ↑最小値＆最大値をO(log(N))で取り出せる
# 要素をO(log(N))で挿入できる

V, E, r = MI()
G = [dict() for i in range(V)]
for i in range(E):
    a, b, c = MI()
    G[a][b] = c
    # list番号が出発点、keyが到着点、valueがcost


# 多重辺があったら入力のところで壊れるので注意
# V=ノード数,E=エッジ数とすると、計算量はO((V+E)logV)
inf = 10**18
MOD = 10**9+7


def Dijkstra(adj, start):
    # adjがstartと隣接するnode,startは出発点
    n = len(adj)
    dist = [inf]*n
    prev = [inf]*n
    # prev[i]:頂点iに至る直前に居た頂点の番号．これを持っておけば，goalからstartまで戻れる
    variety = [0]*(n)  # 最短経路までの道のりは何種類あるか判定
    variety[0] = 1
    dist[start] = 0
    hq = [(0, start)]
    undetermined = n-1  # 枝刈りするためのフラグ
    while hq:
        d, u = heappop(hq)  # hpから最小値を取り出している
        # 最初は 0,startを取り出している
        # 0からstartまで最短経路を出すため
        if dist[u] < d:  # 既により最適な経路がある
            continue
        for v, cost in adj[u].items():  # u -cost-> v
            # 各要素のキーkeyと値valueの両方に対してforループ処理を行いたい場合は、items()メソッドを使う。
            if dist[v] == (dist[u] + cost):
                variety[v] += variety[u]
                variety[v] %= MOD

            elif dist[v] > (dist[u] + cost):
                dist[v] = dist[u] + cost
                variety[v] = variety[u]
                heappush(hq, (dist[v], v))  # hp に　dist[v]とvをpush(追加)している
                # hpに格納しているのは、移動コスト(dist[v])とその場所
                prev[v] = u  # prev[v](現在地)はuという場所からきたことを示している
        undetermined -= 1
        if undetermined == 0:
            # 全点確定後の枝刈り(非連結なら意味はない)
            # 枝刈り探索法の原理
            # 与えられた問題を解くのに，構成要素を１つずつ吟味し，
            # 問題の解決に不必要だと思われるものを冗長なものとして
            # 削除し，縮小された問題を再帰的に解く．
            break
    return dist, variety


L, variety = Dijkstra(G, r)
# 0というGという隣接するnodeを持つ点からスタート
for i in range(V):
    if L[i] == inf:
        print("INF")
    else:
        print(L[i])
    # ここでは　0からi ＆ N-1からiまでの最小値を表示している
