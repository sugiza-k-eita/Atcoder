import bisect
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
ns = LI()
if N == 2:
    print(ns[0], ns[1])
    exit()

ns.sort()
first = ns.pop(-1)
tmp = first/2
# print(tmp)
# print(ns)
_left = bisect.bisect_left(ns,tmp)

if abs(tmp-ns[_left]) > abs(tmp-ns[_left -1]):
    print(first,ns[_left -1])
else:
    print(first, ns[_left])