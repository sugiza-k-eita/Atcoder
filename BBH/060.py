import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
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

N = II()
cnt = [[0]*10 for i in range(10)]

for i in range(1,N+1):
    if i % 10 == 0:
        continue
    num = str(i)
    head = int(num[0])
    tail = int(num[-1])
    # print(num,head,tail)
    cnt[head][tail] += 1

ans = 0
for i in range(1,10):
    for j in range(1,10):
        if i == j:
            ans += cnt[i][j]**2
        else:
            ans += cnt[i][j] * cnt[j][i]
print(ans)