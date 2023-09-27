"""
問題文 日本は N 個の区画に分けられており、西から i 番目の区画（以下、区画 i とする）の標高は A i ​ です。 これから Q 回の地殻変動が起こります。 i 回目の地殻変動では、区画 L i ​ ,L i ​ +1,⋯,R i ​ の標高が V i ​ だけ変化します。（ V i ​ ≥0 のとき標高が ∣V i ​ ∣ 上がり、 V i ​ <0 のとき標高が ∣V i ​ ∣ 下がることを意味します） さて、区画 1 から N へ行く際の不便さは次のように定義されます。 区画 i の標高を E i ​ とするとき、不便さは ∣E 1 ​ −E 2 ​ ∣+∣E 2 ​ −E 3 ​ ∣+⋯+∣E N−1 ​ −E N ​ ∣ 各地殻変動後の不便さをそれぞれ求めてください
"""
N, Q = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    for _ in range(Q):  # Q回のクエリに対応するための出力が必要です。
        print(0)
    exit()

ruiseki = [0] * N
for i in range(N - 1):
    ruiseki[i] = A[i + 1] - A[i]
result = sum(map(abs, ruiseki))

for q in range(Q):
    L, R, V = map(int, input().split())
    L -= 1  # 0-based indexに調整
    R -= 1
    
    if L != 0:
        result -= abs(ruiseki[L - 1])
        ruiseki[L - 1] += V
        result += abs(ruiseki[L - 1])
    
    if R < N - 1:  # ここが間違っていました。
        result -= abs(ruiseki[R])
        ruiseki[R] -= V
        result += abs(ruiseki[R])
    
    print(result)


    