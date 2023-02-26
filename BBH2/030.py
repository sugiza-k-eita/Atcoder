import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import math

N,K = MI()
A = LI()

if N == 1:#N == 1のとき
    if A[0] == K:#A[0]がKの倍数のときのみ
        print("POSSIBLE")
    else:#そうではないのなら
        print("IMPOSSIBLE")
    exit()

max_A = max(A)#A1,A2,・・・Anまでの最大値を取得
#aにA1,A2,・・・Anの最小公倍数を取得する
a = math.gcd(A[0],A[1])
for i in range(2,N):
    a = math.gcd(a,A[i])

if K > max_A:#A1,A2,・・・Anのどの数よりもKのほうが大きいのなら
    print("IMPOSSIBLE")
else:
    if K%a == 0:#A1,A2,・・・Anで得られた最小公倍数でKを表現できる(割り切れる)なら
        print("POSSIBLE")
    else:#そうではないのなら
        print("IMPOSSIBLE")


"""
N個のボールの差分の組み合わせを用いて、Kというボールを作れるか？という問題になります。
今回の問題ではどうゆうときに、Kというボールを作れないかを考えます。

入力例2
3 5
6 9 3　の場合

この場合、どの数の差分をとっても必ず3の倍数になってしまいます。
このことから、A1,A2,・・・Anの最小公倍数がKの約数である必要が有ることがわかります

入力例4
5 12
10 2 8 6 4

この場合、どの数の差分をとってもKより大きい数を作ることができません。
このことから、A1,A2,・・・Anの最大値がKよりも小さい場合は、Kを作ることができず、A1,A2,・・・Anの最大値がKよりも大きい場合は、Kを作れる可能性があります

上記2つの条件より、
A1,A2,・・・Anの最小公倍数がKの約数であり、、A1,A2,・・・Anの最大値がKよりも小さい場合のみ
Kを作ることができることがわかります。
"""