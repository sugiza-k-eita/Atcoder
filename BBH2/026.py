import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

K,T = MI()
A = LI()

max_cake = max(A)
else_cake = K - max_cake
if max_cake > else_cake+1:
    print(max_cake - else_cake -1)
else:
    print(0)


"""
2日連続で食べる可能性が一番高いのは、一番個数の多いケーキです。
そのため、一番個数の多いケーキを配置し、その間にそれ以外のケーキを配置すれば良いです。
もし、
一番個数の多いケーキ <= それ以外のケーキ+1(両端の置くのでそれ以外のケーキが1個少なくても大丈夫)
の場合は、同じケーキを食べる日は0で、

一番個数の多いケーキ > それ以外のケーキ+1の場合は、
max_cake - else_cake -1回同じケーキを食べる日が出てしまう
"""