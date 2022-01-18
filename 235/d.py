from hashlib import new
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

from collections import deque
inf = float("INF")
a,N = MI()
dist = [inf]*(10**6)
dist[1] = 0
que = deque((1,))
while que:
    x = que.popleft()
    new_cost = dist[x] + 1
    nx1 = x*a
    if nx1 < 10**6:
        if new_cost < dist[nx1]:
            dist[nx1] = new_cost
            que.append(nx1)