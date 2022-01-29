import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,K = MI()
ns = LI()
INF = float("inf")
ans = [INF for i in range(N-K+1)]

for i in range(N-K+1):
    ans[i] = min(abs(ns[i]-0),abs(ns[i+K-1]-0))+abs(ns[i]- ns[i+K-1])
print(min(ans))