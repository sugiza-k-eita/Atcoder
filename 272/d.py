from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import itertools


N ,M = MI()
squer = [0]
for i in range(1,10**3+1):
    squer.append(i**2)
move = []
for c in itertools.product(squer,repeat = 2):
    c1,c2 = c[0],c[1]
    if c1+c2 == M:
        root_c1 = int(c1**(1/2))
        root_c2 = int(c2**(1/2))
        # print(root_c1,root_c2)
        move.append((root_c1,root_c2))
        move.append((root_c2,root_c1))
        move.append((-root_c1,root_c2))
        move.append((root_c2,-root_c1))
        move.append((-root_c1,-root_c2))
        move.append((-root_c2,-root_c1))
        move.append((root_c1,-root_c2))
        move.append((-root_c2,root_c1))
        


seen = [[False] * N for i in range(N)]
seen[0][0] = True
dist = [[-1]*N for i in range(N)]
dist[0][0] = 0
def bfs():    
    que = deque()
    que.append([0,0])

    while que:
        now = que.popleft()
        now_y,now_x = now[0],now[1]
        for i,j in move:
            next_y = now_y+i
            next_x = now_x + j
            if 0<=next_x<N and 0<=next_y<N:
                if seen[next_y][next_x] == True:
                    continue
                elif seen[next_y][next_x] == False:
                    seen[next_y][next_x] = True
                    dist[next_y][next_x] = dist[now_y][now_x]+1
                    que.append([next_y,next_x])
    return dist

dist = bfs()
for x in dist:
    print(*x, sep=" ")