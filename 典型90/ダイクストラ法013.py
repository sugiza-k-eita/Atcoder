# 第13問:水diff O((N+M)logN)
from heapq import heappush, heappop
# ↑最小値＆最大値をO(log(N))で取り出せる
# 要素をO(log(N))で挿入できる

N, M = map(int, input().split())
G = [dict() for i in range(N)]
for i in range(M):
    a, b, c = map(int, input().split())
    G[a-1][b-1] = c
    G[b-1][a-1] = c
    # list番号が出発点、keyが到着点、valueがcost


# 多重辺があったら入力のところで壊れるので注意
# V=ノード数,E=エッジ数とすると、計算量はO((V+E)logV)
inf = 10**18


def Dijkstra(adj, start):
    # adjがstartと隣接するnode,startは出発点
    n = len(adj)
    dist = [inf]*n
    prev = [inf]*n
    # prev[i]:頂点iに至る直前に居た頂点の番号．これを持っておけば，goalからstartまで戻れる
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
            if dist[v] > (dist[u] + cost):
                dist[v] = dist[u] + cost
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
    return dist


L = Dijkstra(G, 0)
# 0というGという隣接するnodeを持つ点からスタート
R = Dijkstra(G, N-1)
# N-1というGという隣接するnodeを持つ点からスタート
for i in range(N):
    print(L[i]+R[i])
    # ここでは　0からi ＆ N-1からiまでの最小値を表示している
