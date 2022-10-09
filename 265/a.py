import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

X,Y, N = MI()

three_Apple = Y/3

if N <3:
    print(N*X)
    exit()

if X <= three_Apple:
    print(X*N)
    exit()

else:
    ans = 0
    while N >= 3:
        N -= 3
        ans += Y
    print(ans+X*N)