import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,X = MI()
total = [0]*N
patty = [0]*N
total[0] = 1
patty[0] = 1
for i in range(1,N):
    total[i] += 2*total[i-1]+3
    patty[i] += 2*patty[i-1] + 1

def f(n,x):
    if n==0:
        return 1
    if x<1:
        return 0
    n -= 1
    x-= 1
    if x < total[n]:
        return f(n,x)
    x -= total[n]
