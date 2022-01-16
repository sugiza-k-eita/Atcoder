from collections import Counter
from re import X
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,Q = MI()
ns = LI()
box = []
for i in range(N):
    box.append((ns[i],i))
box.sort()
ns.sort()
import bisect
for q in range(Q):
    x,k = MI()
    left= bisect.bisect_left(ns,x)
    right = bisect.bisect_right(ns,x)
    if right -left +1> k:
        print(box[left+k-1][1]+1)
    else:
        print(-1)

