A = []
B = []
H,W = map(int, input().split())

for i in range(H):
    a = input()
    A.append(a)

for i in range(H):
    b = input()
    B.append(b)

for i in range(H):#縦にi回
    for j in range(W):#横にj回シフト
        cnt = 0
        for k in range(H):
            for l in range(W):#Aのi+k番目j+l番目要素とBのi,jの要素
                if A[(i+k)%H][(j+l)%W] == B[k][l]:
                    cnt += 1
        if cnt == H*W:
            print("Yes")
            exit()
print("No")


"""
2つの二次元リストを、行列好きな方向にシフトして同じものを作れるかという問題です。
両方動かしてできるのなら片方だけを動かしてもできますので、両方動かすのは面倒なので、片方だけ動かすこととします。

今回、実際にシフトさせた配列を毎回作成して、一致するかを試しても良いのですが、
今回は末尾の要素が先頭になるだけなので、配列の並びは変化しません。
そのため、シフトした回数を記憶しておくことで、
n_list[i][j] = origin_list[(i+k)%H][(j+l)%W] 
で求まります。

今回縦にシフトする回数は、最大でもH-1回、横にシフトする回数は、W-1回です。
(H回縦にシフトすると元の配列と一致するため)

そのため、シフトする総回数は(H-1)*(W-1)で、
シフト後すべての点について一致するかを検証するにはH*Wです。
そのため、O(H*W*H-1*W-1)< O(HW^2)< 10**6なので間に合います。
"""