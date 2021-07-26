from collections import Counter
"""
今回iとjについてなので、普通にやるとO(N**2)になってしまいTLE
C問題で極めて頻出のパターン問題で、『同じ値の要素の数をカウントする』
ことでO(N)にすることができる
"""
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
ans = 0
Count_A = Counter(A)
"""
Count_AはAで出てきた数字をカウントしており、例えば１が２回、３が１回だと
Counter({1: 2, 3: 1})
とカウントされる　出てきた回数がindex、カウントされた回数がvalueとなっている
"""

for i in C:
    ans += Count_A[B[i-1]]  # i は　1はじまりなので、pythonに合わせて0始まりにするために-1をしている
"""
for文はCで回す。nで回すのかと思ったが違う。
今回求めたいのはA_i == B[c]であり、Bを求めるには、nではなくcの値を入れる必要がある
また、Count_A[B]では、　Bという数が出てきた回数分、ansに足している

全体の大まかな流れとして、AをCounterしてどの数が何回出てきたか辞書型でCountする
for文でB[c]をindexとしてCount_Aという辞書で索引をかけ、valueの数だけans に足し算する
Aで1が2回出てきていたら、 {1:2} となっており、B[c] = 1の時は、2がansに足される
"""
print(ans)
