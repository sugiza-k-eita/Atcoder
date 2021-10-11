# オイラーツアー
import sys
sys.setrecursionlimit(10 ** 6)
N = int(input())
edge = [[] for i in range(N+1)]
for i in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)
ans = []

# 木上のDFSなので、どの頂点から来たかを引数pで渡せば、訪問済みの頂点を覚えなくても済むらしい


def dfs(u, p):
    # pがどこから来たか
    # uがどこについたか
    ans.append(u)
    for v in edge[u]:
        if v != p:
            #v == pの場合はもと来た場所に戻ってしまうからそれ以外の場合
            dfs(v, u)
            # 行くところなくなったら、戻る処理
            ans.append(u)


for i in range(N+1):
    edge[i].sort()
    # 番号の小さい順に行くからsort()しておく必要がある

dfs(1, -1)
# -1という架空の場所から1という場所に来たことにしている
print(*ans)
