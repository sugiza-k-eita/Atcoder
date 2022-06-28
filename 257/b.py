import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,K,Q = MI()
A = LI()
L = LI()

for i in L:
    i -= 1
    if i == K-1:
        if A[i] == N:
            continue
        else:
            A[i] += 1
    
    else:
        if A[i] + 1 == A[i+1]:
            continue
        else:
            A[i] += 1

print(*A,sep=" ")