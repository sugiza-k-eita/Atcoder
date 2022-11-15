import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import bisect

N = II()
A = LI()

A.sort()

if N == 2:#二個しかなかったら、それを降順にして出力
    print(A[-1],A[0])
    exit()

maximun = A[-1]
harf  = maximun//2
a = bisect.bisect_right(A,harf)
#nの半分(あまりを切り捨てているから大体であるが)の数字がAの中だと何番目に小さいかを取得

if abs(A[a]-harf) > abs(harf-A[a-1]):#indexの前後の値でよりharfに近い方を出力
    print(maximun, A[a-1])
else:
    print(maximun, A[a])

"""
n個の中からr個を選ぶとき
nは大きければ大きいほど、取りうる場合の数は増える
rは、n個のうち、半分を取る時、場合の数は最大となる

なので、Aをソートして、一番うしろ(大きい数)をnとして、
n//2(半分くらい取る)に極力近いrを選択すればよい
"""