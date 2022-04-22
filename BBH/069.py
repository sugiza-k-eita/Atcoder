import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
num = []
for i in range(N):
    a = II()
    num.append(a)

num.sort()

ans = 0
l = 0
r = N-1
cnt = 0
for i in range(N):
    if i %2 == 0:
        
