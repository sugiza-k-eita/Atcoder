import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
box = [[False]*101 for i in range(101)]
known_info = []
known_info_0 = []
for i in range(N):
    x,y,h = MI()
    if h != 0:
        known_info.append([x,y,h])
    elif h == 0:
        known_info_0.append([x,y,h])
    
candidate = []
cnt = 0
for Cx in range(101):
    for Cy in range(101):
        for x,y,h in known_info:
            Ch = abs(Cx-x) + abs(Cy-y) + h
            if box[Cx][Cy] == False:
                box[Cx][Cy] = Ch
                cnt +=1
                continue
            if Ch == box[Cx][Cy]:
                cnt += 1
                if cnt == len(known_info):
                    candidate.append([Cx,Cy,Ch])
            elif Ch != box[Cx][Cy]:
                cnt = 0
                break
# print(candidate)
for Cx,Cy,Ch in candidate:
    for x,y,h in known_info_0:
        if Ch <= abs(Cx-x) + abs(Cy-y):
            continue
        else:
            break
    print(Cx,Cy,Ch)



"""
https://atcoder.jp/contests/abc112/tasks/abc112_c
C - Pyramid

マンハッタン距離を使って、高さを求める
中心から前後左右移動すると1ずつ小さくなる
今回、Cx,Cyはともに0~100の間なので、中心座標の取りうる値は全部で10000通り
そして、Nは100までなので、
Cx,Cy,Nを全探索することが可能です
Cx,Cyを全探索して,N個の情報と矛盾しなければそこが中心座標」

point
しかし、今回高さの最小値がmax(H-|X-Cx| - |Y-Cy|,0)です
なので、0からの距離だと本来の高さよりも大きく出てしまいます
ex)
本来
0,0,0,0
0,0,0,0
0,0,0,1
0,0,1,2

入力
0,?,?,?
0,?,?,?
?,?,0,1
?,?,1,?

の場合、box[0][0]からbox[3][3]までの距離は、6になってしまう。
つまり、h = 0があるところから頂点の位置を推定しようとすると、頂点高さを過大評価してしまう可能性があります。

なので、高さが0以外の座標から、Cx,Cyの高さを求め
その後、Cx,Cyの高さから、h=0のところがちゃんとh=0になるか検証します
"""