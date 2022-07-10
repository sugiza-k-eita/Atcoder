import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,M,X,T,D = MI()

box = [T]* (N+1)

cnt = 0
for i in range(X-1,-1,-1):
    cnt += D
    box[i] -=cnt
    
# for x in box:
#     print(x)
    
print(box[M])     
    