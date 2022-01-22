from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

H,W = MI()
N = II()
ns = LI()
que = deque()
limit = 0
for i in range(N):
    for j in range(ns[i]):
        que.append(i+1)

box = [[0]*W for i in range(H)]
first =que.popleft()
box[0][0] = first

go = [[0,1],[1,0],[0,-1],[-1,0]]
#左に行く、下に行く、右に行く


x = y = 0
while que:
    number = que.popleft()
    for i,j in go:
        if 0<=x+i <H and 0<=y+j <W:
            if box[x+i][y+j] == 0:
                box[x+i][y+j] = number
                x += i
                y += j
                break
            else:
                continue
for xx in box:
    print(*xx, sep=" ")
