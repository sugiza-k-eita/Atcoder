import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
"""
方針
不要なカードの合計が偶数のときはすべて消せる
しかし、不要なカードのうち、最大値と最小値の間に不要なじゃないカードが一枚以上ないとだめ
ない場合、
"""
N = II()
A = LI()
orilen = len(A)
newlen = len(list(set(A)))
if (orilen - newlen)%2 == 0:
    print(newlen)
else:
    print(newlen-1)