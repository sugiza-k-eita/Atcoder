import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
box = []#N個のロボットの右腕,左腕の座標を格納する
for i in range(N):
    X,L = MI()
    head = X-L#i番目の左側に伸びる腕の座標
    tail = X+L#i番目の右側に伸びる腕の座標
    box.append([tail,head])

box.sort()#右腕(tail)が小さい順に格納
#なぜなら、左詰めで配置していくため、tailの値が小さいロボットから配置するかどうかを決めるから

##一番tailが小さいのを配置 
last_tail = box[0][0] #そのtailを記憶
cnt = 1 #カウント
for i in range(1,N):#2体目以降から
    if box[i][1] < last_tail:#もしi番目の左腕(head)の方がi-1番目までに配置すると決めた右腕(tail)の最大値よりも小さいなら配置できない
        continue
    else:#もしi番目の左腕(head)の方がi-1番目までに配置すると決めた右腕(tail)の最大値よりも大きいなら配置できる
        last_tail = box[i][0]
        cnt += 1
print(cnt)

"""
腕の範囲
Xi - Li よりも大きくXi+Liより小さい
(未満と超過の関係なので注意)
としたとき、N個のロボットのうち、それぞれのロボットの腕が被らないようにしたい

どのように配置するかしないかを決めるか？

今回i番目のロボットを置くとしたら、影響が出る範囲はXi - Li からXi+Liの範囲のみです。
そのため、今回は左詰めで配置すると決めたのなら、i番目のロボットが置けるかどうかは、
「i-1番目までのロボットで配置すると決めたロボットの中で一番右側に腕の伸びているロボットと腕が被るかどうか」で決まります。

そのため、これは貪欲法で解くことができます

手順
※head = X-L, tail = X+L
そのため、tailの小さい順に見ていき、
i番目の操作において
「i-1番目までの操作で最後に配置すると決めたロボットのtailよりもi番目のロボットのheadが大きければ(重なっていなければ)配置
重なっている場合は、配置しない
"""
