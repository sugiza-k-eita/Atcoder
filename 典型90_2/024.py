import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


N,K = MI()
A = LI()
B = LI()

sa = 0
for i in range(N):
    sa += abs(A[i]-B[i])
    
if sa <= K and sa%2 == K%2:
    print("Yes")
else:
    print("No")
"""
024 - Select +／- One（★2）
https://atcoder.jp/contests/typical90/tasks/typical90_x

K回の操作でピッタリできる状況は、たくさんありそうなので、K回の操作で、ピッタリ実行できない状況について考えます。

K回の操作できないパターン
Σabs(A[i]-B[i]) > K
K-1,3,5・・・回の操作ですべての数が一致している

の2パターンが考えられます。
条件1については、
それぞれの差分をとって、差分がK以下なら大丈夫です。

条件2について、
K回の操作で一致させるには、K-1回の操作時には、差が1であることが必要です
K-1回の操作で差が1にするには、K-2回の操作時に差が0 or 2である必要があります。
(K-2回目時点で、差が0であっても、K-1回目の操作で1にすることができるから)

このように考えると、実は条件2が条件1の内容を内包していることがわかります。
よって、今回求める条件は、
Σabs(A[i]-B[i]) < K かつ Σabs(A[i]-B[i])%2 == K%2
であるので、その内容を実装していきます
"""