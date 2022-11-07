import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

H,W = MI()

box = []
for i in range(H):
    a = S()
    box.append(a)
    for j in range(W):
        if a[j] == "S":
            start = [i,j]

drdc = [[-1, 0], [1, 0], [0, -1], [0, 1]]
seen = [[False]*W for _ in range(H)]
dist = [[0]*W for _ in range(H)]

def dfs(y,x,prex,prey):
    for dr,dc in drdc:
        nx = x+dr
        ny = y+dc
        if prex == nx and prey == ny:
            continue
        if 0 <= nx < W and 0 <= ny < H:
            if seen[ny][nx]== True or box[ny][nx] == "#":
                continue
            seen[ny][nx] = True
            dist[ny][nx] = dist[y][x]+1
            if ny == start[0] and nx == start[1]:
                break
            dfs(ny,nx,x,y)

dfs(start[0],start[1],-1,-1)

# for x in dist:
#     print(x)
if dist[start[0]][start[1]] >= 4:
    print("Yes")
else:
    print("No")