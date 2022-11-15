import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

H,W = MI()
N = II()
A = LI()
cell = [[-1]*W for i in range(H)]
box = []#どの色が何個あるかを格納
for i in range(N):
    color_num = A[i]
    a = [i+1]*color_num#i番目の色は、color_num個ある
    box+= a
cell[0][0] = box.pop(0)#左上に
def dfs(now_x,now_y,direction):
    if direction == 1:#左→右に探索する場合
        if now_x+1 != W:#右端ではないのなら、
            cell[now_y][now_x+1] = box.pop(0)#一番目の要素をpopするこれにより、1つ前の色と異なるのなら、1つ前の色を使い切ったことに成る
            dfs(now_x+1,now_y,1)
        elif now_x+1 == W:#右端ならば
            if now_y + 1 != H:
                cell[now_y+1][now_x] = box.pop(0)
                dfs(now_x,now_y+1,-1)

    if direction == -1:#右→左に探索する場合
        if now_x-1 != -1:#左端ではないのなら、
            cell[now_y][now_x-1] = box.pop(0)
            dfs(now_x-1,now_y,-1)
        elif now_x-1 == -1:#左端ならば
            if now_y + 1 != H:
                cell[now_y+1][now_x] = box.pop(0)
                dfs(now_x,now_y+1,1)
dfs(0,0,1)#左上から探索
for x in cell:
    print(*x,sep=" ")

"""
探索する順番は
1, 2, 3, 4
8, 7, 6, 5
9,10,11,12
のように進めれば、良いです。

そこで、
偶数行目は現在地から右に向かって探索し
奇数行目は、現在地から左に向かって探索をします。
双方、端にぶつかったら下に降りて、探索する向きを変えます

左上から、
右に向かって探索→右端に着いたら一行下に行く→左に向かって探索→左端に着いたら一行下に行く→右に向かって探索→...
を繰り返して、すべてのマスを探索し終わったら、終わりにします。
"""