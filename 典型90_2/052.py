N = int(input())
box = []
mod = 10**9+7
cnt = 1
for i in range(N):
    A = list(map(int, input().split()))
    A_sum = sum(A)
    cnt *= A_sum
    cnt %= mod
print(cnt)


"""
問題文 
N 個の 6 面体サイコロがあり、 1,2,3,⋯,N と番号付けられています。 サイコロ i の j (1≤j≤6) 番目の面には整数 A i,j ​ が書かれています。ここで、それぞれのサイコロについて、書かれている整数は相異なります。 さて、サイコロの出目に対して、次のように得点を定義します。 得点は N 個のサイコロの出目の総積である。 つまり、サイコロ i の出目を R i ​ としたとき、得点は R 1 ​ ×R 2 ​ ×⋯×R N ​ と計算される。 N 個のサイコロの出目の結果としては 6 N 通り考えられますが、これら全てにおける得点の総和 S を 10 9 +7 で割った余りを求めてください。ただし、それぞれのサイコロは互いに区別できるものとします。

pythonコード
N = int(input())
box = []
mod = 10**9+7
cnt = 1
for i in range(N):
    A = list(map(int, input().split()))
    A_sum = sum(A)
    cnt *= A_sum
    cnt %= mod
print(cnt)

盛り込みたい内容
普通に計算すると、6^^NでTLEになってしまう。
そこで、計算の工夫が必要
"""