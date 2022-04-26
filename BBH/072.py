import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()

def cal(N,h,n):
    bunsi = N*h*n
    bunbo = 4*h*n - N*n - N*h
    if bunbo == 0:
        w = -1.0
    else:
        w = bunsi/bunbo
    return w

for i in range(1,3500):
    for j in range(1,3500):
        w = cal(N,i,j)
        if w.is_integer() and w > 0:
            print(i,j,int(w))
            exit()