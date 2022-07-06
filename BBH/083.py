from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)



H,W = MI()
seen = [[True]*W for i in range(H)]
cnt = [[0]*W for i in range(H)]
#そこについたことがあるかどうか
box = []
que = deque()
for i in range(H):
    A = S()
    for j in range(len(A)):
        #もしi行目j列目が黒なら最初の位置として記録
        if A[j] == "#":
            que.append([i,j])
            seen[i][j] = False
    box.append(A)


moves = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs():
    while que:
        y,x = que.popleft()
        for move in moves:
            new_y,new_x = y+move[0],x+move[1]
            if -1 < new_y < H and -1 < new_x < W:
                if seen[new_y][new_x] == True:
                    cnt[new_y][new_x] = cnt[y][x] + 1
                    seen[new_y][new_x] = False
                    que.append([new_y,new_x])


ans =0
bfs()
for x in cnt:
    ans = max(ans,max(x))
print(ans)