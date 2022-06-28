import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from itertools import combinations
import bisect
N,W = MI()
A = LI()
B = []

for loop in combinations(A,3):
    tmp = sum(loop)
    if tmp <= W:
        B.append(tmp)


for loop in combinations(A,2):
    tmp = sum(loop)
    if tmp <= W:
        B.append(tmp)

for i in A:
    if i <= W:
        B.append(i)

C = list(set(B))
C.sort()
ans = bisect.bisect_right(C,W)
print(ans)


        
