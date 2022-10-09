# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_f
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
    return dist, variety
    #distはスタートからの各nodeまでの最小コストを出力
    #varietyは最小コストで行く方法は何通りあるかを出力

N= II()
dd = {}
inf = 10**18
G = [defaultdict(int) for i in range(N)]#グラフを作成
for i in range(N-1):
    a,b,c = MI()
    a -= 1#indexを0から始めるようにする
    b -= 1#indexを0から始めるようにする
    G[a][b] = c
    G[b][a] = c

Q,K = MI()
node,v = Dijkstra(G,K-1)#K-1　はindexを0から始めるようにする
#node は各ノードがKに行くまでにかかる最短距離
#v は　その最短経路が何個あるか
for i in range(Q):
    x,y = MI()
    x -= 1#indexを0から始めるようにする
    y -= 1#indexを0から始めるようにする
    print(node[x]+node[y])
    #xからk までの最短経路と yからk までの最短経路の和を出力

"""
D - Transit Tree Path
https://atcoder.jp/contests/abc070/tasks/abc070_d


今回も木構造の問題です。今までは、木構造の問題のときは、unionfind or dfs or bfsといっていました。
しかし今回は、別の方法で解きます。その方法とは、ダイクストラ法です。なんで木構造の問題なのに、今までの方法じゃないってわかるかについては、後ほど説明します。
ダイクストラ法とは、負閉路がないように、最短経路を求めるアルゴリズムです。
これにより、dfsやbfsよりも高速に解くことができます。

んじゃ、なぜダイクストラ法とわかるの？
ダイクストラ法の特徴としては、負閉路がないことを保証されている問題にしか使うことができない(強い人なら大丈夫？)代わりに、最短経路を高速で出力できる点です。
今回は、閉路が保証されており、かつ任意の点(K)からのx,yの最短距離を出力する問題です。
なので、ダイクストラ法を使用すると簡単に解くことができます。
"""

