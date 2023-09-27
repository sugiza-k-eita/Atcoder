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

cnt = [[[0,0,0,0] for i in range(W)] for i in range(H)]
INF = float("inf")
from collections import deque

def bfs(rs,cs,H,W):
    que = deque()
    seen = [[[False,False,False,False] for i in range(W)] for i in range(H)]
    dist = [[[INF,INF,INF,INF] for i in range(W)] for i in range(H)]
    for i in range(4):
        dist[rs][cs][i] = 0
        #  up,right,down,left
        que.append([rs,cs,i])
        seen[rs][cs][i] = True


    while que:
        now1,now2,d = que.popleft()
        move = [[-1,0],[0,1],[1,0],[0,-1]]
        mx,my = move[d][0],move[d][1]
        nxt_1,nxt_2 = now1+mx,now2+my
        # print(nxt_1,nxt_2)
        if 0 > nxt_1 or H <= nxt_1 or 0 > nxt_2 or W <= nxt_2:
            continue
        elif maze[nxt_1][nxt_2] == "#":
            continue
        else:
            mini = min(dist[now1][now2])
            for m in range(4):
                # print(nxt_1,nxt_2,mini)
                dist[now1][now2][m] = min(mini+1,dist[now1][now2][m])
            
            for n in range(4):
                # print(nxt_1,nxt_2,n)
                # print(seen[0][0])
                #print(seen[nxt_1][nxt_2][n])
                if seen[nxt_1][nxt_2][n] == True:
                    continue
                if d == n:
                    dist[nxt_1][nxt_2][n] = min(dist[nxt_1][nxt_2][n],dist[now1][now2][d])
                    que.appendleft([nxt_1,nxt_2,d])
                    seen[nxt_1][nxt_2][n] = True
                else:
                    dist[nxt_1][nxt_2][n] = min(dist[nxt_1][nxt_2][n],dist[now1][now2][d]+1)
                    seen[nxt_1][nxt_2][n] = True
                    que.append([nxt_1,nxt_2,n])
            # mini = min(dist[nxt_1][nxt_2])
            # for m in range(4):
            #     # print(nxt_1,nxt_2,mini)
            #     dist[nxt_1][nxt_2][m] = min(mini+1,dist[nxt_1][nxt_2][m])
    return dist
ans = bfs(rs,cs,H,W)
print(min(ans[rt][ct]))
# for h in range(H):
#     print(ans[h])
"""
bfsだからコストが低いやつから探索する必要がある
なので、0costで行けるところを先に探索して、その後1costで行けるところを探索する
Qbfsを二個各必要がある？
que.popleftしたやつをd持ちでrpushすればok?
01bfs

"""



