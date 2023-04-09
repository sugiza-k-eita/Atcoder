import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,K = MI()
edge = [[] for i in range(N)]
loop = []
for i in range(N):
    a = LI()
    if a[i] == 1:
        loop.append(i)
    for j in range(len(a)):
        if a[j] == 1 and i != j:
            edge[i].append(j)

from collections import deque
def bfs(Node,start,N):
    seen = [False]*N
    if start in loop:
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
    
    for i in range(N):
        if seen[i] == False:
            dist[i] = -1
    return dist
dists = []
for i in range(N):
    dist = bfs(edge,i,N)
    dists.append(dist)

Q = II()
for q in range(Q):
    s,t = MI()
    s -= 1
    t -= 1
    ns = s%N
    nt = t%N
    if s == t:
        print(dists[ns][nt])
            
    elif s != t and ns == nt:#nsが等しい
        if dists[ns][nt] == 0:#自己loopあり
            print(1)
        else:#なし
            print(dists[ns][nt])
    else:
        print(dists[ns][nt])

