from collections import deque
import sys
from typing import Collection
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())


N = II()
edge = [[] for _ in range(N)]
for _ in range(N):
    u, k, *v = MI()
    box = []
    for vv in v:
        vv -= 1
        box.append(vv)
    edge[u-1] = box
seen = [True]*N
seen[0] = False
dist = [0]*N
que = deque()
que.append(0)

while que:
    node = que.popleft()
    for nv in edge[node]:
        if seen[nv] == False:
            continue
        seen[nv] = False
        dist[nv] += dist[node] + 1
        que.append(nv)

for dd in range(1, len(dist)):
    if dist[dd] == 0:
        dist[dd] = -1
for i, ans in enumerate(dist):
    print(i+1, ans)
