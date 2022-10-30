import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
ans = 0
tmp = 0
for i in range(N):
    a = II()
    if a != 0:
        tmp += a
    else:
        ans += tmp//2
        tmp = 0
ans += tmp//2
print(ans)

"""
0~Nまでの種類のカードがあります。
一番小さい数から順に見ていき、i番目のカードの枚数が奇数でかつ、i+1番目のカードが0ではない限り、カードを捨てることができます。
逆に言うと、i番目のカードの枚数が0枚のとき、i-1番目が奇数の場合、1枚はペアにすることができません。

なので、0からloopを回して、A[i] == 0の
"""