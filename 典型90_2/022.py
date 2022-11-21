from math import gcd
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

A,B,C = MI()
a = gcd(A,gcd(B,C))
print(A//a+B//a+C//a-3)

"""
022 - Cubic Cake（★2）
https://atcoder.jp/contests/typical90/tasks/typical90_v
立方体の条件について考えます。
立方体とは、縦、横、高さの長さがすべて等しい必要があります。
つまり言い換えると
「すべての辺を同じ長さずつ切断したときにあまりが出ないようにしたい」のです。
よって、3つの辺の長さにおいて、あまりが出ないようにするには、3つの数の最小公倍数をとれば良いです。
(※今回は、切る回数なので植木算のように、切る回数は辺の長さ//最小公倍数から-1になることに注意)
"""