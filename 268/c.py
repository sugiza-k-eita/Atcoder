import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
P = LI()

cnt = 0
box = [[] for i in range(N)]

for i in range(N):
    Pi = P[i]
    box[i] = (Pi-1)%N,Pi%N,(Pi+1)%N


