from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

def bfs(Node,start,N):
    seen = [False]*N
    seen[start] = True
    dist = [0]*N
    que = deque()
    que.append(start)

    while que:
        now = que.popleft()
        for next in Node[now]:
            if seen[next] == True:
                continue
            elif seen[next] == False:
                seen[next] = True
                dist[next] += dist[now]+1
                que.append(next)
    return dist


import collections
N, Q = MI()
ab = [LI() for _ in [None]*(N-1)]
px = [LI() for _ in [None]*(Q)]
ans = [0]*(N)
stack = []
seen = [True]*N
graph = {i: collections.deque() for i in range(0, N)}
for a, b in ab:
    a -= 1
    b -= 1
    graph[a].append(b)
def dfs(u):
    for v in graph[u]:
        if seen[v] == False:
            continue
        seen[v] = False
        ans[v] += ans[u]
        dfs(v)
