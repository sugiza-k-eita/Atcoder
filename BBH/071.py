import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()
B = []
for i in range(N):
    b = A[i] - i
    B.append(b)
B.sort()
middle = B[N//2]
ans = 0
for i in range(N):
    ans += abs(A[i] - middle - i)
print(ans)
