import collections
import sys
from typing import Coroutine, Counter, no_type_check_decorator
sys.setrecursionlimit(10**6)
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())


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


for p, x in px:
    p -= 1
    ans[p] += x

dfs(0)

print(*ans)
