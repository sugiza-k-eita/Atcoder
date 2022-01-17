import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M = MI()
ns = LI()
ns.sort()

from bisect import insort_left

for i in range(M):
    x = ns.pop()
    x //= 2
    insort_left(ns,x)
print(sum(ns))
