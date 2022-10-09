import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,M,T = MI()

A = LI()
for m in range(M):
    X,Y = MI()
    A[X-1] -= Y
time = T*-1
for i in range(N-1):
    time += A[i]
    if time < 0:
        continue
    else:
        print("No")
        exit()
print("Yes")