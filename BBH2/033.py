import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = II()
A = LI()

ans = [0]*N
cnt = 0
for i in range(N):
    if i %2 == 0:
        cnt += A[i]
    else:
        cnt -= A[i]
ans[0] = cnt//2

for i in range(N-1):
    ans[i+1] = A[i]-ans[i]

for i in range(N):
    ans[i] += ans[i]
print(*ans, sep=" ")
