import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, K = MI()
X = LI()
if N == K == 1:
    print(X[0])
    exit()
ans = float("inf")
for i in range(N-K+1):
    L = X[i]
    R = X[i+K-1]
    zero_L_R = abs(0-L)+abs(L-R)
    zero_R_L = abs(0-R)+abs(L-R)
    ans = min(ans,zero_L_R,zero_R_L)
print(ans)

"""
N本のうち、K本のろうそくを付ける必要があります。
その際につけるろうそくの組み合わせはnCkで今回の制約だとTLEしてしまいます。
そこで、今回の問題の特徴を深掘りしていきます。

今回は、通った区間のろうそくであれば火をつけることができます。
つまり、2つのろうそくを選んだらその区間にある全てのろうそくは必ず火がつくことになります。

そのため、今回はK本のろうそくに火をつけたいので、
0~Nの任意のiについて、i本目とi+K-1本目の2つのろうそくに火をつけたら必ずK本以上のろうそくに火をつけることができます。
これにより、線形時間で問題を解くことができます。

手順

"""