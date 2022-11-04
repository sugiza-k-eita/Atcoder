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
A.sort()#対象レーティングをソートしておく
C = []#何点以上ならどのクラスになるかを表すしきい値
for i in range(N-1):
    c = (A[i+1]+A[i])//2#対象レーティングが何点以上ならi番目のクラスになるかを求める
    C.append(c)
# print(C)
Q = II()
for q in range(Q):
    b = II()
    ind = bisect.bisect_left(C,b)
    #しきい値C[ind]なので、A[ind]のクラスが一番絶対値の差が小さい
    ans = abs(b-A[ind])
    print(ans)

"""
対象レーティングと生徒のレーティングの差が小さいクラスに入れれば良い
今回、制約がN = Q= 3*10**5なので
Q人の生徒に対して、N個のクラスを総当りで全探索したら間に合いません。
Qではどうするか？

今回、N個のクラスの対象レーティングは決まっているので、予めソートしておき、何点以上何点以下ならどのクラスに分類されるかわかります。
そのため、はじめに

その後、Q人の生徒において、
配列2分法(名称が違ったらごめんなさい)を用いてどのクラスが適正かを求めます。
※配列2分法は、ソートされている配列(長さN)に対し、ある数xが何番目に位置するかをO(log(N))で求めることのできるアルゴリズムです。
これにより、O(Q log(N))なので間に合う

pythonの場合は、bisectというライブラリを使用することで楽に実装できます。

競技プログラミングで使うライブラリの一覧表見たいのがほしい・・・
"""