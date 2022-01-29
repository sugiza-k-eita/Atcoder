import functools
import math
import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,K= MI()
ns = LI()
if K in ns:
    print("POSSIBLE")
    exit()


gc = functools.reduce(math.gcd,ns)
# made = []
# iter = max(ns)//gc
# for i in range(iter-1):
#     made.append(max(ns)-gc)

if K%gc == 0 and max(ns)>=K:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")
