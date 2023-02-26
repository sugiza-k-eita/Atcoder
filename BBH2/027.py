import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 8)

#pypyだとTLEだからpython3.8系で実行

N,Q = MI()
edge = [[] for i in range(N)]# 各頂点がどこの頂点とつながっているかを格納
for i in range(N-1):
    a,b = MI()
    a -= 1#0-indexにしたいので-1
    b -= 1#0-indexにしたいので-1
    edge[a].append(b)#辺を追加
    edge[b].append(a)#辺を追加

cnt = [0]*N#各頂点に加算される値
for j in range(Q):
    p,x = MI()
    p -= 1#0-indexにしたいので-1
    cnt [p] += x

seen = [True]*N#flg
seen[0] = False
def dfs(u):#uを根(親)に持つ子に対してdfs
    for v in edge[u]:
        if seen[v] == False:#根に戻ることはだめ
            continue
        else:
            seen[u]  = False#2度と訪れないようにする
            cnt[v] += cnt[u]#i番目の頂点の値 = 自分に加算されている値 + 自分の根に加算されている値
            dfs(v)#vを根(親)に持つ子に対してdfs

dfs(0)

print(*cnt, sep=" ")


"""
各頂点において、
i番目の頂点 = i番目の頂点に加算された値 + 自分の親に加算された値
です。

ここで重要なのは、i番目の値はi番目の頂点に加算された値と自分の親に加算された値の2つの値によってのみ決まります。

一見、i番目の頂点から根までのすべての頂点の値を持ってないと行けなそうですが、その必要はありません。
ex)
親  子  孫
+3 +2 +1の場合、

子は自分の値+2と親の値+3の合計の+5を持ち、
親  子  孫
+3 +5 +1

孫は自分の値+1と子の値+5の合計の+6を持ちます
このように、親から順に実行することで、自分と自分の親のみの2つの値のみで加算される値を管理できます。


そのため、根(親)から順に葉(子)に対してdfs or bfsを行うことで実装できます。
"""