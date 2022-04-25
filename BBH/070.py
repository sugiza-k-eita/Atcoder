import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import bisect
N = II()
A = LI()
A.sort()
B = LI()
B.sort()
C = LI()
C.sort()

ans = 0
for i in range(N):
    middle = B[i]
    A_ok = bisect.bisect_left(A,middle)
    C_ok = N - bisect.bisect_right(C,middle)
    ans += A_ok*C_ok
print(ans)
    


