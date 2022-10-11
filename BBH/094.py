import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,K = MI()

def comb(n, r, m):
    X, Y = 1, 1
    for i in range(r):
        X *= n-i
        Y *= i+1
        X %= m
        Y %= m
    return int(X * pow(Y, m-2, m))


for i in range(1,K+1):
    ans = comb(N-K+1,i,10**9+7)#青いボールの分け方
    ans *= comb(K-1,i-1,10**9+7)#赤いボールの分け方
    print(ans%(10**9+7))

# """
# D - Blue and Red Balls
# https://atcoder.jp/contests/abc132/tasks/abc132_d

# 青いボールは連続して取ることが可能なので、問題を言いかえると「青が連続しているブロックがi個となる並び方は何通りありますか」という問題に変形できます。


# 手順
# 青をiグループに分ける
# 赤をi+1に分ける
# ２つの事象は独立なので、かけて出力です。

# 手順1
# 青をiグループに分ける
# 今回、青をi個のグループに分けることができたら、その間に赤を置けば良いです。
# ex) 4つの青球を3つに分ける
# 青青青青||
# これに関しては、4つの青球と2つのしきい棒があれば、コンビネーションで解くことができます。
# (4+2)C2
# しかしこれだけでは不十分です。なぜなら
# 青青青青||のように、1つの青グループと、2つの空集合のように空の集合ができてしまうためです。

# なので、先に必ず置くところに先に1個づつおいておくことにすれば問題を解決できます。
# なので、ボールの分け方は、
# ex) 4つの青球を3つに分ける
# 先に3つの青玉をおいておく
# 残った青球としきい棒を求める
# で空集合を許容しない形で青球を分けることが可能です。
# f(x,y) = x個のボールをy個のグループに分ける(空集合不可)
# →g(x,y) = x-y個のボールをy個のグループに分ける(空集合可)
# g(x,y)は、空集合があってもはじめに取り除いたy個のボールをそれぞれのグループに加算できるから

# 赤玉も同様の手順で求めることができます。
# 赤玉は、青球の間に入れなきゃいけないので、i-1個に関しては、置き方が決められます。
# しかし、残ったR-i+1個は青球の間に置くか両端に置くかできるので、置ける場所はi+1通りになります。
# なので、R-i+1Ci+1です。


# """