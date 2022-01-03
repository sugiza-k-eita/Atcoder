import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

M,N = MI()

def power(x, y):
    mod = 10**9+7
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y/2)**2 % mod
    else:
        return power(x, int(y/2))**2 * x % mod


ans = power(M, N)
print(ans)