import collections
#Pythonの標準ライブラリのcollectionsをインポートします。
#これにより、リスト内の要素の出現回数を数えるCounter関数を使用できます。
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# 空のリストnA, nB, nCを作成します。
# これらのリストは、リストA, B, Cの各要素を46で割った余りを格納します。
nA = []
nB = []
nC = []
for i in range(N):
    nA.append(A[i]%46)
    nB.append(B[i]%46)
    nC.append(C[i]%46)

#collections.Counter関数を使用して、リストnA, nB, nCの各要素の出現回数を数えます
count_A = collections.Counter(nA)
count_B = collections.Counter(nB)
count_C = collections.Counter(nC)

cnt = 0
#3つのforループを用いて、0から45までの全ての組み合わせについて、選んだ3つの数（i, j, k）の合計が46の倍数になるかどうかを確認します。
for i in range(46):
    for j in range(46):
        for k in range(46):
            if (i+j+k)%46 == 0:#もし46の倍数になるなら、
                cnt += count_A[i]*count_B[j]*count_C[k]#その組み合わせの数（各リスト内で該当する数の出現回数の積）をカウンタcntに加算します
print(cnt)


"""
制約N < 10^5より、配列全てに対して探索すると、O(N^3)の計算量が必要となり、現実的な時間内に計算を完了させることが難しい。そこで、計算量を削減するための工夫が求められる。

では、どのようにリストを圧縮するか？今回は、(A[i]+B[j]+C[k])%46 == 0となる組み合わせを見つけたいので、各リストの各要素を46で割った余りを考慮すればよい。
(なぜなら(a + b) mod n = [(a mod n) + (b mod n)] mod nより上記のモジュラ算術の性質を利用します。それぞれの数A[i], B[j], C[k]を46で割った余りを求め、それらの和を46で割った余りが0である組み合わせを見つければ、元の3つの数の和が46の倍数である組み合わせを見つけることができます)

このようにすることで、リスト内の要素がどのような値であっても、その余りは0から45の間の46種類に圧縮される。

そのため、A,B,Cのリスト内の要素について46で割ったときの余りを求め、それらの値の出現回数をカウントする。この操作により、それぞれの余りがいくつ存在するのかが把握でき、それらを組み合わせる計算を効率的に行うことが可能となる。

その後、全ての可能な余りの組み合わせについて、その和が46の倍数となるかどうかを確認すればよい。もし46の倍数となる組み合わせがあれば、その組み合わせの数（該当する余りの出現回数の積）を合計することで、最終的に求めるべき組み合わせの総数を得ることができる。
-------------
"""