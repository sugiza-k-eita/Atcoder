import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


N,M = MI()
node = [[] for i in range(N)]
reverse_node = [[] for i in range(N)]

for m in range(M):
    A,B = MI()
    A -= 1
    B -= 1
    node[A].append(B)#辺の向きが正しい向きのグラフを作成
    reverse_node[B].append(A)#辺の向きが逆向きのグラフ


box = []#帰りがけ順記憶するbox　nodeの番号を追加していく
seen = [True for i in range(N)]#訪れたことがあるかのflg

#手順1でのdfs
def dfs(u):
    seen[u] = False#訪れたので、false
    for v in node[u]:
        if seen[v] == False:#そこに訪れたことがあるのなら探索しない
            continue
        dfs(v)
    box.append(u)#戻ってきたタイミングでuを追加


compornents = []#強連結成分ごとに格納
#手順2での逆向きのグラフに対して行うdfs
def reverse_dfs(u):
    seen[u] = False
    compornents[-1].append(u)#一番うしろのグループに追加
    for v in reverse_node[u]:
        if seen[v] == False:
            continue
        reverse_dfs(v)

for i in range(N):
    if seen[i] == False:#到達済みのnodeは探索しない
        continue
    dfs(i)


box.reverse()#帰りがけ順が大きい数字から探索したいので、reverse
seen = [True for i in range(N)]#flgをリセット
for i in box:
    if seen[i] == False:#到達済みのnodeは探索しない
        continue
    compornents.append([])#まずcompornentsにからのリストを追加し、そこに強連結成分を追加していく
    reverse_dfs(i)

ans = 0
for i in compornents:
    n = len(i)#１グループに含まれるノード数
    ans += n * (n-1)//2#nC2が双方に行き来できるということ
print(ans)


"""
021 - Come Back in One Piece（★5）
https://atcoder.jp/contests/typical90/tasks/typical90_u

今回は、強連結成分を求める問題です。
強連結成分とは、
有向グラフにおいて、任意の2点が双方に行き来できるような成分
のことです。
ex)
1 ↔ 2
1 → 2, 2 → 3, 3 → 1

今回は、その強連結成分が何個のグループからなるかを求める問題です。

先に解法をお伝えしますと、工夫したdfsを二回行うとできます。
詳しくは、こちらの記事をご参照ください。

手順
前処理
入力で与えられる有向グラフ(=node)と、矢印の向きが逆の有向グラフ(=reverse_node)を作成する。

1~Nまでの点において、探索していない頂点から帰りがけ順dfsを行う

帰りがけ順の大きい頂点から、探索していない頂点からreverse_nodeに対し、dfsを行う

これで互いに行き来できる強連結成分に分解することができます。
"""