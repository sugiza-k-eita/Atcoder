from collections import deque
from bisect import insort_left
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M = MI()
ns = LI()


for i in range(M):
    b,c = MI()
    box = [c]*b
    ns.extend(box)
ns.sort()
ans = sum(ns[-N:])
print(ans)