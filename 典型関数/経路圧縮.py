#https://atcoder.jp/contests/abc228/tasks/abc228_d
#https://qiita.com/u2dayo/items/e80a489c6e7472da3d83#d%E5%95%8F%E9%A1%8Clinear-probing
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = 2**20
Q = II()

def find(x): #xの根を求める
    if par[x] < 0:
        #親がいないのなら自分自身を返す
        return x
    else:
        par[x] = find(par[x])
        #親がいるのなら、一番上の親を返す
        return par[x]

def unite(x,y): #xとyの属する集合の併合
    x = find(x)
    y = find(y)
    # if x > y: x,y = y,x  #必ずx<=y
    # if y == N-1: x,y = y,x
    if x == y:
        return False
    else:
        par[y] += par[x]
        par[x] = y
        return True

#初期化
#根なら-size,子なら親の頂点
par = [-1]*N
ans = [-1]*N
for i in range(Q):
    t,x = MI()
    xN = x%N
    if t == 1:
        if ans[xN] == -1:
            #空いていたらそのまま代入
            ans[xN] = x
            h = xN
            #根の構造を更新するためにhを持つ
        else:
            h = (find(xN)+1)%N
            #空いてなかった場合は、自分の親の一つとなりに格納
            ans[h] = x

        if ans[(h-1)%N] != -1:
            unite((h-1)%N, h)
            #もし自分の-1の場所が埋まっていたら、自分と自分-1をくっつける
        if ans[(h+1)%N] != -1:
            unite(h, (h+1)%N)
            #もし自分の+1の場所が埋まっていたら、自分と自分-1をくっつける

    else:
        print(ans[xN])