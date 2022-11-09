import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

H,W = MI()
Q = II()
from typing import List

class UnionFind:
    """0-indexed"""

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n

    def unite(self, x, y) -> bool:
        """xとyをマージ"""
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        self.__group_count -= 1

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return True

    def is_same(self, x, y) -> bool:
        """xとyが同じ連結成分か判定"""
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        """xの根を取得"""
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x) -> int:
        """xが属する連結成分のサイズを取得"""
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """全連結成分のサイズのリストを取得 O(N)
        """
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        """全連結成分の内容のリストを取得 O(N・α(N))"""
        groups = dict()
        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)
        return list(groups.values())

    @property
    def group_count(self) -> int:
        """連結成分の数を取得 O(1)"""
        return self.__group_count

uf = UnionFind(H*W)#H*Wのnodeを用意
box = [[0,1],[0,-1],[-1,0],[1,0]]#隣接するマス
flg = [[False]*W for i in range(H)]#そのマスが赤マスかどうかを判断
for q in range(Q):
    query= LI()
    if len(query)==3:#query1なら
        r,c = query[1],query[2]
        r -= 1#0始まりのindexに直すため-1
        c -= 1
        flg[r][c] = True# そのマスを赤マスにする
        for x_y in box:#隣接するマスの探索
            y = x_y[0]+r
            x = x_y[1]+c
            if -1 < y < H and -1 < x < W:#隣接するマスがH*Wの範囲内で
                if flg[y][x]== True:#かつ赤マスなら
                    uf.unite(y*W+x,r*W+c)#連結
    
    else:#query2なら
        ra,ca,rb,cb = query[1],query[2],query[3],query[4]
        ra -= 1#0始まりのindexに直すため-1
        ca -= 1
        rb -= 1
        cb -= 1
        if flg[ra][ca] == True and flg[rb][cb] == True:#2点が赤マスで
            if ra == rb and ca == cb:#そもそも2点が同じ点なら
                print("Yes")
                continue
            if uf.is_same(ra*W+ca,rb*W+cb):#2点が連結可能なら
                print("Yes")
            else:
                print("No")
        else:
            print("No")

"""
https://atcoder.jp/contests/typical90/tasks/typical90_l
012 - Red Painting（★4）


query1
(r,c)のマスを赤くする
→隣接する赤マスがあればそのマスと連結可能である
query2
(ra,ca)から(rb,cb)へ到達可能か？
→これまでのquery1の操作を通して、(ra,ca)と(rb,cb)は連結されているか？

今回、2点間が連結可能か、もしくは連結されているかを判別する必要があることがわかりました。
そのため、連結判定を高速で行えるunionfindを用いて実装していきます。

unionfindとは、グラフ系の問題でよく出てくる典型解法で、
2点間を繋いだり、
連結されているかを判別する
典型解法なので、今回の問題にぴったりです。

前処理？
まず、H*Wの二次元のマス目なので、それをグラフで扱いやすくするため1配列にしていきます。
i = r * W + c とすることで、二次元配列を1つのノードに変換します。
また、(r,c)が赤マスかを判別するためにH*Wのflgという2次元配列を用意しておきます。

if query1
flg[r][c] = True と、そのマスが赤マスの印を立てて置きます。
その後、隣接する4マスについて、H*Wマスの範囲内でかつ、赤マスなら連結させます。
探索するノード
i1 = (r-1)*W +c
i2 = (r+1)*W +c
i3 = r * W +c+1
i4 = r* W + c-1

if query2
(ra,ca),(rb,cb)が両方とも赤マスかつ
連結されているのなら
Yesを返します。
"""