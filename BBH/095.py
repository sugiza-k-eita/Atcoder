import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()
zero_cnt = [0]*60
one_cnt = [0]*60
mod = 10**9 + 7

for i in range(N):
    x = list(reversed(format(A[i], '060b')))
    for j in range(60):
        if x[j] == "0":
            zero_cnt[j] += 1
        elif x[j] == "1":
            one_cnt[j] += 1

# print(zero_cnt)
ans = 0
for j in range(60):
    ans += zero_cnt[j]*(one_cnt[j])*pow(2, j)
    ans %= mod

print(ans%mod)
"""
各桁ごとにloopを回す
k桁目の sum(xor) は、1の個数 * 0の個数で求まる。
なぜなら、 0 xor 0 = 1, 0 xor 1 = 1, 1,xor 1 = 0 より
任意の(i,j)が(0,1) or (1,0)の場合のみ1を取るため
0の個数(X)と1の個数(Y)の掛け算で、求まる
"""