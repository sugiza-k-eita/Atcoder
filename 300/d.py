import math
import bisect

def Eratosthenes(N):
    N += 1
    is_prime_list = [True] * N
    m = int(N ** 0.5) + 1
    for i in range(3, m, 2):
        if is_prime_list[i]:
            is_prime_list[i * i :: 2 * i]=[False] * ((N - i * i - 1) // (2 * i) + 1)
    return [2] + [i for i in range(3, N, 2) if is_prime_list[i]]

N = int(input())
sosuu = Eratosthenes(math.ceil((N)**(1/2)))
cnt = 0
for i in range(len(sosuu)):
    a = sosuu[i]
    if a**5 > N:
        break
    for j in range(i+1,len(sosuu)):
        b = sosuu[j]
        if a*a*b*b*b > N:
            break
        tmp_c = (N/(a*a*b))
        max_c = (tmp_c)**(1/2)
        aaa = bisect.bisect_right(sosuu,max_c)
        cnt += aaa - j - 1
print(cnt)


"""
本問題は、Nyaan様の解説をもとに作成しています。

今回の問題は、a^2*b*c^2<Nとなるような素数の組み合わせを求める問題です。
ここでa,b,cという3つの変数のうち、それぞれの取りうる範囲は
a
a**5 < a^2*b*c^2<Nより
a < N^(1/5)
b
a=2のとき、2^2 * b * c^2 < 2^2 * b^3< N
b < (N/4)^(1/3)<N^(1/3)

c
a=2,b = 3のとき
2^2*3*c^2 < N
c^2 < N/12
c < (N/12)^(1/2)<N^1/2

つまり、

しかしa,b,cの取りうる値すべての組み合わせについて全探索すると
N1/5*1/3*1/2
で時間が足りません。

なので工夫して全探索する必要があります。
そこで事前に素数のリストを用意しておき、累積和のようにすることで計算量を落とすことができます。
例えば、aとbの値が決まればcの取りうる範囲は
b+1以上で(N/a*a*b)**1/2以下の素数になります。
上記の範囲の素数の個数は、
(N/a*a*b)**1/2以下の素数の個数-b以下の素数の個数で求まります。
これにより、aとbが求まれば、cの取りうる範囲の素数の個数O(1)で求まります。

a,bについての全探索は
1/5;1/3で8/15なので、10**7以下なのでギリギリ探索できます。
"""