import sys
sys.setrecursionlimit(10 ** 7)


N = int(input())

nodes = [[] for i in range(N)]#各頂点がどの頂点とのパスを持つか格納するリスト
for i in range(N-1):
    a,b = map(int, input().split())
    a -= 1#0-indexにしたいので-1
    b -= 1
    nodes[a].append(b)#頂点aは、bへのパスを持つ
    nodes[b].append(a)


A = [1 for i in range(N)]#自分のパスよりも下の部分木の個数を格納するためのリスト
flg = [True for i in range(N)]#flg
flg[0] = False

def dfs(v):
    for nv in nodes[v]:#現在地vからnvへ行く
        if flg[nv] == False:#既に訪れていたら
            continue
        else:#初めて訪れたら
            flg[nv] = False#二度と訪れないようにflgを更新
            dfs(nv)#nvについて部分木を探索
            A[v] += A[nv]#nvまでの部分木の合計を加算

dfs(0)
ans = 0
for i in range(N):
    ans += A[i] * (N-A[i])
print(ans)

"""
039 - Tree Distance（★5）
https://atcoder.jp/contests/typical90/tasks/typical90_am
考える上で
この章は、解説ではないので読み飛ばしても大丈夫です
解説に至るまでの考えを書いてます

各頂点(i)から、それ以外の頂点(else_i)への距離の総和を求める問題です
各頂点からの最短距離は、ダイクストラ法を用いれば計算量はO((V+E)logV)
#Vは頂点数、Eが辺数
で求まります。

しかしこれをすべての頂点について行うと
O(V((V+E)logV)//2) > O(V^2) > 10^8となりTLEとなってしまいます。
見積もり違ったらすみません。

そのため、ダイクストラ法を用いて解くのは難しいです。
そこで頂点に注目するのではなく、辺に注目します。
具体的には、
すべての2点間において最短経路で移動した際にそれぞれの辺は何回使用されたか
について考えます。

考察
以下のような木構造があった場合、
赤い辺を使用するのは、
赤い辺よりも下にある[]とそれ以外の[]間の移動のときだけです。
このことから、任意の辺の使用回数は
その辺よりも下にある辺の数(部分木)*それ以外(N-部分木の数)で求まります。

その辺よりも下にある辺の数(部分木)はdfs(O(V+E))で求めることができるので、dfsで求めた後、各辺の使用された回数を計算すればTLEすることなく答えにたどり着けます
"""