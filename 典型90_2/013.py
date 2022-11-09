import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

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
    dist = [inf]*n#初期値をinfに固定
    prev = [inf]*n
    # prev[i]:頂点iに至る直前に居た頂点の番号．これを持っておけば，goalからstartまで戻れる
    variety = [0]*(n)  # 最短経路までの道のりは何種類あるか判定
    variety[0] = 1 #0→0は1通りしかないため
    dist[start] = 0
    hq = [(0, start)]
    undetermined = n-1  # 枝刈りするためのフラグ
    while hq:
        d, u = heappop(hq)  # hpから最小値を取り出している
        # 最初は 0,startを取り出している
        # 0からstartまで最短経路を出すため
        if dist[u] < d:  # もし既により最適な経路がある
            continue
        for v, cost in adj[u].items():  # 同じコストの最適な経路が見つかったら
            if dist[v] == (dist[u] + cost):
                variety[v] += variety[u] #uの場所まで行く最短経路のpath分だけ、vに行くまでの最短経路が増える
                variety[v] %= MOD

            elif dist[v] > (dist[u] + cost): # 新しく最短経路が見つかった場合
                dist[v] = dist[u] + cost
                variety[v] = variety[u] #uの場所まで行く最短経路のpath分だけ、vに行くまでの最短経路がある
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

N,M = MI()
dd = {}
inf = 10**18
G = [defaultdict(int) for i in range(N)]
for i in range(M):
    a,b,c = MI()
    a -= 1 #indexを0始まりにする
    b -= 1 #indexを0始まりにする
    G[a][b] = c
    G[b][a] = c

dist1,v= Dijkstra(G,0) #0番目の頂点から各頂点までの最短経路　indexは0始まりのため、1ではなく0
distN,v = Dijkstra(G,N-1) #N-1番目の頂点から各頂点までの最短経路indexは0始まりのため、NではなくN-1

for i in range(N):
    print(dist1[i]+distN[i])

"""
013 - Passing（★5）
https://atcoder.jp/contests/typical90/tasks/typical90_m

今回の問題は、
1番目の都市からk番目の都市に行くまでにかかる時間の最小値
N番目の都市からk番目の都市に行くまでにかかる時間の最小値
(双方向なので、k↔Nは同じコスト)
合計を求める問題です。

今回のように、ある1つの頂点から各頂点までの最短経路を高速で求めるには、ダイクストラ法を用いる方法です。
ここでは、ダイクストラ法の概要だけお話します。ダイクストラ法についての詳しい解説は、こちらの記事はわかりやすくまとまっていますので、ご参照ください。
https://qiita.com/knhr__/items/cb3ce311508337128714
ダイクストラ法の計算量は、O((N+M)logN)である頂点から各頂点までの最短経路を求めることができますので、事前に1番目からのi番目の最短経路とN番目からi番目の最短経路を求めておけば、計算時間は間に合います。
(※ダイクストラ法は、閉路やマイナスのコストがあると使えないので注意)
"""