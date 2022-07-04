import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
import math
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,K =MI()
A = LI()
mod = 10**9+ 7

p = 0
q = 0
for i in range(N-1):
    for j in range(i+1,N):
        if A[i] > A[j]:
            p += 1

q = 0
for i in range(N):
    for j in range(N):
        if A[i] > A[j]:
            q += 1

ans = (p*K + q*(K-1)*K//2) % mod
print(ans)