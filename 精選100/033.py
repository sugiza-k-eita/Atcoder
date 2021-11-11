from collections import deque
import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


H, W = MI()
max_ans = H*W
area = [S() for _ in range(H)]
cnt = 0
for i in range(H):
    for j in range(W):
        if area[i][j] == "#":
            cnt += 1
drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
seen = [[False]*W for _ in range(H)]
dist = [[0]*W for _ in range(H)]
start = [0, 0]
que = deque()
que.append(start)

while que:
    y, x = que.popleft()
    seen[y][x] = True
    for dr, dc in drdc:
        nx = x+dr
        ny = y+dc
        if 0 <= nx < W and 0 <= ny < H:
            if seen[ny][nx] or area[ny][nx] == "#":
                continue
            seen[ny][nx] = True
            dist[ny][nx] = dist[y][x]+1
            que.append([ny, nx])
            if seen[H-1][W-1] == True:
                ans = max_ans - cnt - dist[H-1][W-1]-1
                print(ans)
                exit()
print(-1)
