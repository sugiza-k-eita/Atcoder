import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
box = [[] for i in range(N)]
for i in range(N):
    box[i] = S()

dp = [[0]*(N+1) for i in range(N+1)]
"""
そこが白ならconti
黒なら探索開始
"""

for i in range(N):
    for j in range(N):
        #横に探索
        cnt = 0
        for x in range(6):
            if x +i == N:
                break
            if box[i+x][j] == "#":
                cnt += 1
        if cnt == 4:
            print("Yes")
            exit()
        cnt = 0
        #縦に探索
        for y in range(6):
            if y + j== N:
                break
            if box[i][j+y] == "#":
                cnt += 1
        if cnt == 4:
            print("Yes")
            exit()
        cnt = 0
        #ななめに探索
        for z in range(6):
            if z +i== N or z+j == N:
                cnt = 0
                break
            if box[i+z][j+z] == "#":
                cnt += 1
        if cnt >= 4:
            print("Yes")
            exit()

        #ななめに探索
        cnt = 0
        for z in range(6):
            if i+z== N or j-z == -1:
                cnt = 0
                break
            if box[i+z][j-z] == "#":
                cnt += 1
        if cnt >= 4:
            print("Yes")
            exit()
        
print("No")