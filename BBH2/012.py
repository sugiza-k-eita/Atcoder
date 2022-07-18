from collections import Counter
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
D = LI()


# D.sort()

c = Counter(D)

if c[0]!=1 or D[0]!=0:
    print(0)
    exit()

ans = 1
mod = 998244353

for i in c.keys():
    if i>=1:
        ans*=(pow(c[i-1],c[i]))
        ans%=mod
print(ans%mod)


