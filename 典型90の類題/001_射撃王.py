import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
box = []
for i in range(N):
    h,s = MI()
    box.append([h,s])

def check(mid):
    timer = []
    for i in range(N):
        x = mid
        h,s = box[i][0],box[i][1]
        x -= h #xまでの残り高度
        t = x//s#距離(高度) / 速さ　で時間を求める
        timer.append(t)
    timer.sort()#優先順位が高い順にソート
    for i in range(N):
        if i > timer[i]:
            return False
    return True


# 最大値を求める
higest = 0
for i in range(N):
    h,s = box[i][0],box[i][1]
    higest = max(higest,h+s*N)

lowest  = -1

# 2分探索
cnt = 0
while higest - lowest > 1:
    mid = (lowest + higest)//2
    # 真ん中を調べる
    if check(mid):
        # すべての風船をmid以下のの時間で割ることができるなら
        higest = mid
    else:
        lowest = mid
    # print(lowest,higest)
print(higest)

"""
すべての風船を高度X以内に割ることができるかどうかとする
今回N個の風船を1秒ごとに割ることができるので、
Xの取りうる値の最大値は、N番目に割ったときに一番高い位置higest=max(H1+NS1, H2+NS2 ・・・Hn+NSn)
Xの取りうる値の最小値は,1となる

1 < X < higest
(higestは, =H+N*Sより　最大で10**(5+9)なので、2分探索なら間に合う)

高度Xを前回の最小値と最大値の平均から求める
N個の風船が高度xになるまでに何秒かかるかを求める
ソートして、優先順位の高い(すぐ高度xになる風船)から割っていく
すべてを割ることができたら、高度x以下で、割ることができなかったら高度X以上という範囲の絞り込みを2分探索
1,2,3,4を繰り返す
"""