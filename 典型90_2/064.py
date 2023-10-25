#事前に計算
"""
問題文 日本は N 個の区画に分けられており、西から i 番目の区画（以下、区画 i とする）の標高は A i ​ です。 これから Q 回の地殻変動が起こります。 i 回目の地殻変動では、区画 L i ​ ,L i ​ +1,⋯,R i ​ の標高が V i ​ だけ変化します。（ V i ​ ≥0 のとき標高が ∣V i ​ ∣ 上がり、 V i ​ <0 のとき標高が ∣V i ​ ∣ 下がることを意味します） さて、区画 1 から N へ行く際の不便さは次のように定義されます。 区画 i の標高を E i ​ とするとき、不便さは ∣E 1 ​ −E 2 ​ ∣+∣E 2 ​ −E 3 ​ ∣+⋯+∣E N−1 ​ −E N ​ ∣ 各地殻変動後の不便さをそれぞれ求めてください
"""
N, Q = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    for _ in range(Q):  # Q回のクエリに対応するための出力が必要
        print(0)
    exit()

inconvenience = [0] * N#各地点での不便さを格納
for i in range(N - 1):
    inconvenience[i] = A[i + 1] - A[i]
result = sum(map(abs, inconvenience))

for q in range(Q):
    L, R, V = map(int, input().split())
    L -= 1  # 0-based indexに調整
    R -= 1
    
    if L != 0:
        result -= abs(inconvenience[L - 1])#地殻変動が起きたら、L-1~Lの不便さを引き、
        inconvenience[L - 1] += V#新しい不便さに更新し
        result += abs(inconvenience[L - 1])#それを合計の不便さに足す
    
    if R < N - 1:  
        result -= abs(inconvenience[R])
        inconvenience[R] -= V
        result += abs(inconvenience[R])
    
    print(result)


"""
不便さが変化するのは、
L-1~L間とR~R+1間のみ

そのため、事前に各地点での不便さを計算しておき、全体の不便さを計算しておきます
L~R間で地殻変動が起こったら、
1.地殻変動前のL-1~LとR~R+1の不便さを全体の不便さから引き、
2.L-1~LとR~R+1の不便さを更新
3.L-1~LとR~R+1の不便さを全体の不便さに足す



不便さの計算
各地点(i)での不便さはA[i+1]-A[i]とする
ex)
1 2 3
1 1
そのため、不便さの長さはN-1となります。
"""

