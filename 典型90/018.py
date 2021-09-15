# 今回の問題は立体の対角線を求める問題と置き換えることができそう
# そのため、E8さんと高橋さんの座標を求めて、
# 差分を2乗して足して√
# 三角関数
# x = 0
# y = -L/2* sinΘ
# z = L/2* cosΘ
import math
T = int(input())
L, X, Y = map(int, input().split())

p = [X, Y, 0]
# 高橋君の座業


def where(t):
    theta = 2*math.pi*t/T
    return [0., -L/2*math.sin(theta), L/2*(1-math.cos(theta))]
    # E8さんの座標


Q = int(input())
for i in range(Q):
    e = int(input())
    q = where(e)
    height = q[2]
    tmp_leng = math.sqrt((p[0]-q[0])**2 + (p[1]-q[1])**2)
    angle = math.atan2(height, tmp_leng)
    print(math.degrees(angle))
    #   距離を求めた
    # tmp_leng2 = (p[0]-q[0])**2 + (p[1]-q[1])**2 + (p[2]-q[2])**2
    # leng2 = math.sqrt(tmp_leng2)
    # print(leng)
