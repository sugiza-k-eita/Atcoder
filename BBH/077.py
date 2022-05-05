import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

H,W,A,B = MI()

box = [[0]*W for i in range(H)]

for i in range(B):
    for j in range(A,W):
        box[i][j] = 1

for i in range(B,H):
    for j in range(A):
        box[i][j] = 1
        
for xx in box:
    print(*xx,sep="")
    