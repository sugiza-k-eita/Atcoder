import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


a,b,c = MI()
if a < c**b:
    print("Yes")
else:
    print("No")


"""
020 - Log Inequality（★3）
https://atcoder.jp/contests/typical90/tasks/typical90_t

aの値が大きすぎて、普通に計算するのは厳しいです。
また、logやrootは計算過程で誤差が発生するので、比較するのが難しい
なので、このままの状態では、2つの数字を比較することは難しいです。

ではどうするか？？
誤差が発生しない(発生しづらい)整数に変換して比較する

logの場合、2つの数の大小関係は
ex) log a ,b logc
    →a ,c**bの大小関係と等しくなる。
よって、この性質を使って問題をときます。


"""