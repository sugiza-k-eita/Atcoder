import sys
sys.setrecursionlimit(10000)
# よくわからないけど、↑これがないとREになる
# 再帰条件を上げるっていう意味があるらしい
# dfs 深さ優先


def dfs(u):
    if seen[u] == True:
        return ans[u]

    for v in edge[u]:
        ans[u] = max(dfs(v)+1, ans[u])
    seen[u] = True
    return ans[u]


N, M = map(int, input().split())

edge = [[] for i in range(N)]
ans = [0]*N
seen = [False]*N
for i in range(M):
    first, end = map(int, input().split())
    edge[first-1].append(end-1)

for i in range(N):
    dfs(i)

print(max(ans))
print(ans)
print(seen)
