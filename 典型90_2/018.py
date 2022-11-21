import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import math

T = II()
L,X,Y = MI()
def angle(x,y,z):
    leng_X = X-x
    leng_Y = Y-y
    XY = (leng_X**2+leng_Y**2)**(1/2)
    radian = math.atan2(z,XY)
    print(math.degrees(radian))
    
Q = II()
for q in range(Q):
    E = II()
    degree = 360*E/T#度数法
    theta = math.radians(degree)#度数法から弧度法に変換
    y,z = -L/2*math.sin(theta),L/2 -L/2*math.cos(theta)#観覧車の位置を求める
    angle(0,y,z)


"""
https://atcoder.jp/contests/typical90/tasks/typical90_r
018 - Statue of Chokudai（★3）

弧度法と度数法を使って求める問題です。
俯角を求めるには、

観覧車の位置を求める
観覧車と高橋直大像の高さの差、距離の差を求める
arctanで俯角を求める
という流れになります。

観覧車の位置(観覧車が反時計回りなのに注意)
y軸,z軸方向の変化は、
0   90 180  270 360
0 → -L →0 → L → 0
0 →L/2 →L →L/2 → 0
となります。よって、式に直すと、
y = -L/2*math.sin(theta)
z = L/2 -L/2*math.cos(theta)
※ thetaは弧度法での値
となります。

ここから、観覧車の位置から直大像のxy平面上の距離とz方向の高さの差を求めます。
xy平面上の距離
(直大像のx座標位置-観覧車のy座標位置)^2 +  (直大像のy座標位置-観覧車のy座標位置)^2
z方向の高さの差
観覧車のz座標の位置(直大像の高さは0のため)

最後に、arctanを使って、俯角を求めます。
mathライブラリに、辺の長さから角度(弧度法)を求める事のできる関数があるので、それを用います。
"""