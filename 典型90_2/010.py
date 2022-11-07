import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
class_A = [0 for i in range(N)]
class_B = [0 for i in range(N)]

for i in range(N):
    c,p = MI()
    if c == 1:
        class_A[i]=p
    else:
        class_B[i]=p

Q = II()
ruiseki_A = [0]
ruiseki_B = [0]

for i in range(N):
    ruiseki_A.append(ruiseki_A[-1]+class_A[i])
    ruiseki_B.append(ruiseki_B[-1]+class_B[i])

# print(ruiseki_A)
# print(ruiseki_B)
for q in range(Q):
    l,r = MI()
    l -= 1
    
    ans_A = ruiseki_A[r]-ruiseki_A[l]
    ans_B = ruiseki_B[r]-ruiseki_B[l]
    print(ans_A,ans_B)
    
"""
https://atcoder.jp/contests/typical90/tasks/typical90_j
010 - Score Sum Queries（★2）

結論から先にいうと今回は、累積和を用いる問題です。
問題は
学籍番号が1~Nの連番で決められていて、そのN人が2つのクラス(AクラスとBクラスとします)に割り振られている。※(1組の1番の人と2組の1番の人が同時に存在しない)
任意の区間で、A組の人の合計とB組の人の合計点数を出力しなさい
という問題です。

制約が、N == Q <= 10**5なので、Q回の操作で、N人の人のクラスと点数を毎回計算するとTLEしてしまいます
Question ではどうするか？
事前に0からi番目までの合計点数を計算しておく

これにより、LからRまでの区間を0~L の合計点数 - 0~(R-1)の合計点数　で求めることができます。
このように、0からi番目の累積された数字を持つ典型解法を累積和といいます。
事前に累積和を計算しておくことで、任意の区間の合計点数を出力するのは、O(1)で行うことができますので、Q人の回のクエリにおいて実行しても間に合います。
"""