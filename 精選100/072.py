import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

H,W = MI()
mod = 10**9 +7
total = H +W -2
#total Combination H をする
def comb(n, r, mod=10**9 + 7):
    p = 1
    for i in range(r):
        p *= (n - i) * pow(i + 1, mod-2, mod)
        p = p % mod
    return p

ans = comb(total,H-1)
print(ans)
