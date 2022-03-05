import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
mod=10**9 + 7
N,A,B = MI()
def comb(n, r, mod=10**9 + 7):
    """
    nCr を modを法として求める
    計算量はO(r)
    modがNoneの場合は modを取らない結果を返す
    mod はNoneか素数であることを仮定する
    """
    p = 1
    for i in range(r):
        p *= (n - i) * pow(i + 1, mod-2, mod)
        p = p % mod
 
    return p

a = comb(N,A)%mod
b = comb(N,B)%mod
z = pow(2,N,mod) -1
ans = z-a-b
print(ans %mod)
