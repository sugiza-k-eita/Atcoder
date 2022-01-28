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

    if x >= 10 and x % 10 != 0:
        nx2 = int(str(x % 10) + str(x // 10))  # 文字列で結合したあと、整数に戻すのが楽でしょう
        if new_cost < dist[nx2]:
            dist[nx2] = new_cost
            que.append(nx2)
if dist[N] != inf:
    print(dist[N])
else:
    print(-1)