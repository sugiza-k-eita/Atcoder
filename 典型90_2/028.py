import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


N = II()
xy = [[0]*1001 for i in range(1001)]#(1000,1000)マス目は(1000,1000),(1000,1001),(1001,1000),(1001,1001)から成るため、
for i in range(N):
    lx,ly,rx,ry = MI()
    xy[ly][lx] += 1#左上の頂点と右下の頂点には+1
    xy[ry][rx] += 1
    xy[ly][rx] += -1#左下の頂点と右上の頂点には-1
    xy[ry][lx] += -1

#xy[y軸情報][x軸方向]　今回、x軸が横軸、y軸が縦軸なのに注意
for i in range(1001):#上から
    for j in range(1,1001):#行方向に累積和
        xy[i][j] += xy[i][j-1]

for j in range(1001):#左から
    for i in range(1,1001):#列方向に累積和
        xy[i][j] += xy[i-1][j]


# for x in xy:
#     print(x)

from collections import defaultdict
d = defaultdict(int)

for i in range(1001):
    for j in range(1001):
        d[xy[i][j]] += 1#面積のカウント

for i in range(1,N+1):
    print(d[i])

"""
028 - Cluttered Paper（★4）
https://atcoder.jp/contests/typical90/tasks/typical90_ab

今回は、2次元空間上に重なる紙の面積を求める問題です。
Nが10^5であるため、1回あたりの計算量はO(1)である必要があります。
なので、今回は、前処理の段階で、k枚重なっている部分の面積を計算しておく必要がありますｌ．
そこで、今回は、2次元にもす法を使ってときます。

2次元いもす法とは、
要素の重複を効率良く行う解法であるいもす法を2次元に拡張した解法
(いもす法についてはこちらの記事がわかりやすいです)
https://imoz.jp/algorithms/imos_method.html

今回の場合の2次元いもす法は、
左上の頂点と、右下の頂点に+1
左下の頂点と、右上の頂点に-1として
※座標とマス情報を混同しないように

手順
上から順に行方向(x方向)に累積和を取る
左から順に列方向(y方向)に累積和を取る

そうすることで、
左上、左下、右上、右下の範囲で囲まれた部分の面積はすべて1となる。

先程も書いたが、扱っている情報は、マス目情報ではなく、頂点情報であるため
左上の頂点から左下の頂点までの辺の距離は、(ry-ly-1)です
左上の頂点から右上の頂点までの辺の距離は、(rx-lx-1)です
(私はこれを勘違いして2時間くらいさまよってました)
扱っている情報は、頂点座標の情報ですが、「その頂点はいくつ分の重なるを持つか？」という風に考えることで、面積の重なりを表しています。(たぶん)
"""