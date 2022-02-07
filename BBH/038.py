from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


H,W = MI()
box = [[] for i in range(H)]

for i in range(H):
    box[i] = S()
    for j in range(W):
        if box[i][j] == ".":
            sx,sy = i,j
            break
que = deque()
que.append([sx,sy])
go = [[0,1],[0,-1],[1,0],[-1,0]]
dist = [[-1]*W for i in range(H)]
dist[sx][sy] = 0
mx,my = 0,0
while que:
    z= que.popleft()
    x,y = z[0],z[1]
    for xi,yi in go:
        nx = x+xi
        ny = y + yi
        if -1 < nx < H and -1 < ny < W:      
            if dist[nx][ny] == -1 and box[nx][ny] == ".":
                dist[nx][ny] = dist[x][y] + 1
                mx,my= nx,ny
                que.append([nx,ny])


que = deque()
que.append([mx,my])
dist = [[-1]*W for i in range(H)]
dist[mx][my] = 0
while que:
    z= que.popleft()
    x,y = z[0],z[1]
    for xi,yi in go:
        nx = x+xi
        ny = y + yi
        if -1 < nx < H and -1 < ny < W:      
            if dist[nx][ny] == -1 and box[nx][ny] == ".":
                dist[nx][ny] = dist[x][y] + 1
                que.append([nx,ny])

ans = 0
for xx in dist:
    ans = max(ans,max(xx))
print(ans)
"""
木の直径を出す
そこから探索する

"""

    
