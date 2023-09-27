import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,Q = MI()
points = []
nx_s = []
ny_s = []
for i in range(N):
    x,y = MI()
    nx = x-y
    ny = x+y
    nx_s.append(nx)
    ny_s.append(ny)

max_nx = max(nx_s)
max_ny = max(ny_s)
min_nx = min(nx_s)
min_ny = min(ny_s)


for j in range(Q):
    q = II()
    q -= 1
    nx,ny = nx_s[q],ny_s[q]
    ans = max(abs(nx-min_nx),
              abs(nx-max_nx),
              abs(ny-min_ny),
              abs(ny-max_ny))
    print(ans)