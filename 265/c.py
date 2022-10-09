import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

H,W = MI()
wall = []
for i in range(H):
    tmp = S()
    wall.append(tmp)

seen = [[True]*W for _ in range(H)]

seen[0][0] = True
def dfs(i,j):
    direction = wall[i][j]
    if direction =="U" and i == 0:
        print(i+1,j+1)
        exit()
    elif direction == "D" and i == H-1:
        print(i+1,j+1)
        exit()
    elif direction == "L" and j == 0:
        print(i+1,j+1)
        exit()
    elif direction == "R" and j == W-1:
        print(i+1,j+1)
        exit()
    
    else:
        if seen[i][j] == False:
            print(-1)
            exit()
        else:
            seen[i][j] = False
            if direction == "U":
                ni,nj = i-1,j
            elif direction == "D":
                ni,nj = i+1,j
            elif direction == "L":
                ni,nj = i,j-1
            elif direction == "R":
                ni,nj = i,j+1
            dfs(ni,nj)
dfs(0,0)