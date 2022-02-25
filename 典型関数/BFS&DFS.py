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

"""
https://atcoder.jp/contests/abc239/tasks/abc239_e
順序のある木構造
"""

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(u, p):#uが現在地でpは一つ前の場所
    L[u].append(A[u])  # 自分自身に書かれた整数
    for v in G[u]:
        if v == p:
            continue
        dfs(v, u)
        L[u].extend(L[v])  # uの子vの部分木の整数をすべてuに追加
    L[u].sort(reverse=True)  # 大きい順なので、reverse=True
    L[u] = L[u][:MAX_K]  # 20個に減らします

MAX_K = 20
N,Q = MI()
A = [0] + LI()#indexを入力に合わせるためにはじめに0を追加する
G = [[]  for i in range(N+1)]
L = [[] for _ in range(N + 1)]  # 頂点iの部分木に書かれた整数を大きい順に最大20個記憶
for i in range(N-1):
    a,b = MI()
    G[a].append(b)
    G[b].append(a)

dfs(1,0)#0というノードからきた1という数字がもつ木の探索
for j in range(Q):
    v,k = MI()
    print(L[v][k-1])