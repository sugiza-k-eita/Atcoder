import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from itertools import product
from bisect import bisect_left, bisect_right
N = II()
rep = len(str(N))
box = []

for bit3 in product("0357", repeat=rep):
    num = ""
    for i in range(rep):
        num += str(bit3[i])
    box.append(int(num))
ans = []
for aa in box:
    aa = str(aa)
    if "3" in aa and "5" in aa and "7" in aa and "0" not in aa:
        ans.append(int(aa))

anser = bisect_right(ans,N)
# print(ans)
print(anser)
