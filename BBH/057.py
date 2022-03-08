import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()

#区間dp or 累積和のどちらか
#計算量的に累積和だと思う

ruiseki = [0]
s = 0
for i in range(N):
    s+= A[i]
    ruiseki.append(s)

from collections import Counter
counted = Counter(ruiseki)
ans = 0
for j in counted.values():
    ans += j*(j-1)//2
print(ans)
