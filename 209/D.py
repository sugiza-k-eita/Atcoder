from collections import deque
que = deque()
N, Q = map(int, input().split())
G = [[] for i in range(N)]
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)

dist = [-1]*N
que.append(0)
dist[0] = 0
# dist0は0にする
while que:
    now = que.pop()
    for next in G[now]:
        if dist[next] == -1:
            # そこに一度も訪れたことがないのなら
            dist[next] = dist[now]+1
            que.append(next)
            # そこからまたqueの処理をする

for i in range(Q):
    c, d = map(int, input().split())
    c -= 1
    d -= 1
    if dist[c] % 2 == dist[d] % 2:
        print("Town")
    else:
        print("Road")
# ｃから1番目の都市につく際に通る都市の偶奇と、dから0番目の都市につく際に通る都市の偶奇が一致していれば
# どこかの都市で会える
