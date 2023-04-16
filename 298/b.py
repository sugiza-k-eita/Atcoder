N = int(input())
A_box = []
B_box = []

for i in range(N):
    A = list(map(int, input().split()))
    A_box.append(A)

for i in range(N):
    B = list(map(int, input().split()))
    B_box.append(B)


for q in range(4): #今回は、右回転を4回行っています
    for i in range(N):
        for j in range(N):
            if B_box[i][j] == 0 and A_box[i][j] == 1:
                #もしA[i][j]が1なのにB[i][j]が1じゃないならだめ
                break
        else:
            continue
        break
    else:#breakされなかった。つまりすべての点においてしA[i][j]=B[i][j]=1なら
        print("Yes")
        exit()
    
    #回転させる
    A_box = A_box[::-1]#上下転置
    new_A_box = []#右回転した新しい配列を格納するlist
    for x in zip(*A_box):
        new_A_box.append(x)#転置
    A_box = new_A_box#右回転したリストをA_boxに代入　これでA_boxが右回転した

#4回のfor文処理が終わったのに、Yesが出力されてなければ
print("No")

"""
B - Coloring Matrix
https://atcoder.jp/contests/abc298/tasks/abc298_b
入力
N:文字列
A[i][j]: Aのi行目j列目
B[i][j]: Bのi行目j列目

今回、Aを回転させたときに、A[i][j]==1のとき、B[i][j]==1が成り立つかどうかを判定するプログラムを書きたいです

ここで、回転させる回数は、(初期位置で判定していない場合)最大でも4回になります。なぜなら4回回転させるとともとの形に戻るためです。
そこで、4回右回転or左回転をさせるには、
右回転:上下入れ替え→転置
左回転:転置→上下入れ替え
を行うことで回転させることができます。

2次元配列の上下入れ替えるためには、list名[::-1]で上下入れ替えができ、
2次元配列の転置は、zip()を使うことで転置できます。
"""