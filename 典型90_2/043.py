H,W = map(int, input().split())

rs,cs = map(int, input().split())
rs -= 1
cs -= 1
rt,ct = map(int, input().split())
rt -= 1
ct -= 1

maze = []
for i in range(H):
    s = input()
    maze.append(s)

INF = float("inf")
from collections import deque
que = deque()
dist = [[[INF,INF,INF,INF] for i in range(W)] for i in range(H)]
for i in range(4):
    dist[rs][cs][i] = 0
    #  up,right,down,left
    que.append([rs,cs,i])
# print(que)

move = [[-1,0],[0,1],[1,0],[0,-1]]
#urdl
while que:
    x,y,d = que.popleft()
    nx = x+move[d][0]
    ny = y+move[d][1]

    if 0 > nx or H <= nx or 0 > ny or W <= ny:
        continue
    elif maze[nx][ny] == "#":
        continue
    for nd in range(4):
        if d == nd:
            if dist[nx][ny][nd] > dist[x][y][d]:
                que.appendleft([nx,ny,nd])
            dist[nx][ny][nd] = min(dist[x][y][d],dist[nx][ny][nd])
        else:
            if dist[nx][ny][nd] > dist[x][y][d]:
                que.append([nx,ny,nd])
            dist[nx][ny][nd] = min(dist[x][y][d]+1,dist[nx][ny][nd])


print(que)
for i in dist:
    print(i)

print(min(dist[rt][ct]))
# # for h in range(H):
# #     print(ans[h])
"""
最小の方向変換

cost0のところを優先的に探索したい
deque で

"""



