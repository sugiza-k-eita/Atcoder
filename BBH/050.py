from collections import deque
from dis import dis
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

"""
BFSで最短経路を求めそれ以外を黒く塗る
"""

H,W =MI()
box = [[] for i in range(H)]
cnt = 0
for  i in range(H):
    box[i] = S()
    cnt += box[i].count("#")




que = deque()
que.append([0,0])
go = [(0,1),(1,0),(-1,0),(0,-1)]
seen = [[True]*W for i in range(H)]
INF = float("inf")
dist =[[INF]*W for i in range(H)]
dist[0][0] = 0
seen[0][0] = False
while que:
    x,y = que.popleft()
    for i,j in go:
        nx = x + i
        ny = y + j
        if 0 >nx or nx >= W or 0 >ny or ny >= H:
            continue
        if box[ny][nx] == "#":
            continue
        if seen[ny][nx] == False:
            continue
        dist[ny][nx] = dist[y][x] + 1
        seen[ny][nx] = False
        que.append([nx,ny])

if dist[-1][-1] == INF:
    print(-1)
    exit()

black = H*W -dist[-1][-1]
# print(black)
ans = black -cnt
print(ans-1)


# for xx in dist:
#     print(xx)