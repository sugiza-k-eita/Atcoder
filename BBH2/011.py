import sys
from typing import Counter
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)




A,B = MI()
def tameshi(n):
    ret = []
    for i in range(2, int(n ** (1 / 2)) + 1):
        if i > n:break
        while n % i == 0:
            n //= i
            ret.append(i)
    if n != 1:
        ret.append(n)
    return ret


a = tameshi(A)
b = tameshi(B)
a.append(1)
a = list(set(a))
b.append(1)
# print(a,b)

kouyaku = []
for i in range(len(a)):
    if a[i] in b:
        kouyaku.append(a[i])

print(len(kouyaku))

"""
https://atcoder.jp/contests/abc142/tasks/abc142_d
D - Disjoint Set of Common Divisors

今回の問題は、手を動かしてみると意外と難しかったりします。
公約数を出した後、いくつかの公約数を選択し、そのすべてがお互いに素でないといけないためです。

ではどうするか？
今回大事なのは、選ばれた数2つがお互いに素であり、かつAとBの公約数ということです。

なので、
はじめにAとBの公約数を求めるのではなく、AとBに対しそれぞれ素因数分解を行います。
その後、得られたAの素因数とBの素因数の共通している部分を抽出します。
抽出された数字は、素数なのでどの2つの数字を選んでもお互いに素になりますし、お互いの約数であることは自明です。
"""