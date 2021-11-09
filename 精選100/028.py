from collections import deque
import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


R, C = MI()
x_s, y_s = MI()
x_g, y_g = MI()
x_s -= 1
y_s -= 1
x_g -= 1
y_g -= 1
c = [S() for _ in range(R)]
seen = [[False]*C for _ in range(R)]
dist = [[0]*C for _ in range(R)]
que = deque()
que.append([x_s, y_s])
drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
while que:
    x, y = que.popleft()
    for dr, dc in drdc:
        nx = x+dr
        ny = y+dc
        if 0 <= nx < R and 0 <= ny < C:
            if seen[nx][ny] or c[nx][ny] == "#":
                continue
            seen[nx][ny] = True
            dist[nx][ny] = dist[x][y]+1
            que.append([nx, ny])
print(dist[x_g][y_g])
