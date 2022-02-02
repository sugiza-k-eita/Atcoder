"""
方針
減少が1倍なあらH1-Hnの最大値が楽しさの最大値
減少が2倍なので、
楽しさ = H1 - Hn - (登った高さ)
楽しさ = H1 - (Hn + 登った高さ)
Hn + 登った高さ の最小値を求める
Hnは与えられているので、登った高さの最小値をダイクストラ法で出力し、その値とHnの合計が最小のものが良い
"""

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
    return dist
    #distはスタートからの各nodeまでの最小コストを出力
    #varietyは最小コストで行く方法は何通りあるかを出力

N,M = MI()
h = LI()
node = [defaultdict(int) for i in range(N)]
for i in range(M):
    u,v = MI()
    u -= 1
    v -= 1
    u_v = max(h[v]-h[u],0)
    v_u = max(h[u]-h[v],0)
    node[u][v] = u_v
    node[v][u] = v_u

raise_height = Dijkstra(node,0)

ans = 0

for i in range(N):
    ans = max(ans,h[0] -(h[i]+raise_height[i]))
print(ans)