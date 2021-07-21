"""
今回の問題は、a→b,b→c　の時、a→cの道路がなくても行ける
そのため、a→bに行ける場合は、都市bから行ける都市すべてが都市aからでも行けることを示している。
よって、dfs（深さ優先探索）を行う
Trueを保つ場合は、その地点からdfsを行う
注　a→c　と　a→b→c　では経路が違うが始点と終点が等しいため、1つとして数えなければならない
そのため、リストの中に、始点の数だけFalseデータをもたせ、到着できた地点にはtrueのデータをもたせる。
これにより再度到着した際にif文ですでにTrueだったらカウントしない or　Trueを再代入するようにする
"""

import sys
sys.setrecursionlimit(10000)
# よくわからないけど、↑これがないとREになる
# 再帰条件を上げるっていう意味があるらしい

# dfs 深さ優先


def dfs(u):
    for v in edge[u]:
        if not seen[v]:
            seen[v] = True
            dfs(v)


n, m = map(int, input().split())
edge = [[] for i in range(n)]
# edgeは始点の数だけ設け、その中に移動先の年のデータをもたせる
for i in range(m):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)  # roadは0始まりなので、-1することで合わせている
    # a番目の都市のデータに、到着できるｂのデータを格納している

ans = 0
# 始点をfor文で回している
for i in range(n):
    seen = [False]*n  # 始点であるiから移動できるところをtrueで返す
    seen[i] = True  # 始点と終点が同じところはtrue
    dfs(i)
    """
    # dfs 深さ優先
    def dfs(u):
        for v in edge[u]:           #edgeは始点(a)から移動できる点(b)の情報を持っているリストで
            if not seen[v]:         #a番目のリストには移動できるbの情報が格納されている
                seen[v] = True      #a(i)番目の都市からb(v)番目の都市に移動できる場合Trueにして、その後v番目の都市から行ける都市についてdfsしている
                dfs(v)
    """
    ans += seen.count(True)

print(ans)
