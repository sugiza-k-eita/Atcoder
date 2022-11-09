import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A,B,C = MI()
ans = 9999
for i in range(10000):
    for j in range(10000-i):
        blance = N -A*i-B*j
        if blance < 0:
            break
        if blance%C == 0:
            cnt = blance//C
            ans = min(ans,i+j+cnt)
print(ans)


"""
016 - Minimum Coins（★3）
https://atcoder.jp/contests/typical90/tasks/typical90_p

今回は、制約が解く上で重要な鍵になってきます。(問題文でも太字になっています)
合計 9999 枚以下の硬貨でちょうど N 円を支払うことができる
つまり、
A 円硬貨をi枚、B 円硬貨をj枚使った場合
払わなけらばならない残金は
balance  = N - (A*i + B*j)
使用できるC 円硬貨枚数は、最大でも　
cnt = 9999-(i+j)枚しか使えません。

このことから、A円硬貨を使う枚数(i)とB円硬貨を使う枚数(j)をそれぞれ0から9999までで、全探索することで、C円硬貨を何枚使うかわかります。
よって、払わなければならない残金(blance)がC円硬貨でピッタリ払い切れる場合の
硬貨の合計枚数が一番小さい値を記憶しておき、出力すればよいです。
"""