import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

mod = 998244353
A,B,C,D,E,F = MI()
A %=mod
B %=mod
C %=mod
D %=mod
E %=mod
F %=mod

A_B = A*B %mod
A_B_C = A_B*C %mod
D_E = D*E%mod
D_E_F = D_E*F %mod
ans = (A_B_C - D_E_F)%mod
print(ans)