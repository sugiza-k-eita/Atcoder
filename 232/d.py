from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

H,W = MI()
c = [S() for _ in range(H)]
seen = [[False]*W for _ in range(H)]
dist = [[0]*W for _ in range(H)]
dist[0][0] = 1
que = deque()
que.append([0,0])
drdc = [[1, 0], [0, 1]]
while que:
    x, y = que.popleft()
    for dr, dc in drdc:
        nx = x+dr
        ny = y+dc
        if 0 <= nx < H and 0 <= ny < W:
            if seen[nx][ny] or c[nx][ny] == "#":
                continue
            seen[nx][ny] = True
            dist[nx][ny] = dist[x][y]+1
            que.append([nx, ny])

ans = 1
for i in dist:
    tmp_ans = max(i)
    ans = max(tmp_ans,ans)

print(ans)