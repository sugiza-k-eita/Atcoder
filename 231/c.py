import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
import bisect
N,Q = MI()
ns = LI()
ns.sort()
leng= len(ns)
for i in range(Q):
    x = II()
    index = bisect.bisect_left(ns,x)
    print(leng-index)