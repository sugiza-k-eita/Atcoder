from collections import deque
import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


H, W, N = LI()
area = [S() for _ in range(H)]
factory = {}
for i in range(H):
    for j in range(W):
        if area[i][j] == "S":
            y_s, x_s = i, j
        if area[i][j].isdigit():
            factory[int(area[i][j])] = [i, j]
drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
seen = [[False]*W for _ in range(H)]
dist = [[0]*W for _ in range(H)]
que = deque()
que.append([y_s, x_s])
cnt = 1
while que:
    if cnt == N+1:
        print(dist[factory[cnt-1][0]][factory[cnt-1][1]])
        exit()
    y, x = que.popleft()
    seen[y][x] = True
    for dr, dc in drdc:
        nx = x+dr
        ny = y+dc
        if 0 <= nx < W and 0 <= ny < H:
            if seen[ny][nx] or area[ny][nx] == "X":
                continue
            seen[ny][nx] = True
            dist[ny][nx] = dist[y][x]+1
            que.append([ny, nx])
            if [ny, nx] == factory[cnt]:
                seen = [[False]*W for _ in range(H)]
                cnt += 1
                que.clear()
                que.append([ny, nx])
                break
