import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,L  = MI()
K= II()
A = LI()




def check(x):
    num = 0
    # 何個に切れたか
    pre = 0
    # 前回の切れ目の位置
    for i in range(N):
        if A[i] - pre >= x:
            # 前回の切れ目の位置からぜんざいの切れ目の位置の長さがx以上なら
            num += 1
            pre = A[i]
    # 最後のピースがx以上なら加算
    # これがK+1の+1の部分
    if L - pre >= x:
        num += 1

    if num >= K + 1:
        return True
    else:
        return False
    # 分割した個数がK+1(切った回数+1)になったらreturn


# 2分探索
left, right = -1, L+1

while right - left > 1:
    # right は今回　L+1 でleftがLのときは
    # L+1 -L = 1になるからその時にbreakが起きるようになっている？
    mid = (left + right)//2
    # 真ん中を調べる
    if check(mid):
        # すべてのようかんをmid以上の長さにできるのなら
        left = mid
    else:
        right = mid
print(left)



"""
今回は、K+1分割した羊羹の中で、最小の羊羹の大きさを最大化する問題です。
N < 10**5
L < 10**9
最小の羊羹の大きさをMとすると、Mの取りうるサイズは
0< M < <= Lです。
なので、Mを0からLの大きさでloopを回して、Lcmの羊羹について、Mcmの羊羹をK個以上作れるかを判別すれば答えが出ます

しかし、今回制約が、Lが10**9なので、0~Lについて全探索することが無理できないということです。
ではどうしましょう・・・？
AAer 2分探索を行う
上記でも示しましたが、Mの取りうるサイズは
0< M < <= Lです。
ですが、例えば、Mが10cm以上であることがわかれば、Mが0~9cmなのか探索する必要がなるなります。
なぜなら、M=10であるのであれば、それ以下の数字は、答えになりえないためです。
また、Mが20cm以下であることがわかったとします。その場合、21~Lについて探索する必要はなくなります。
なぜなら、M< 20であるのであれば、それ以上の数字は答えになりえないためです。
このように全探索しなくても、徐々に範囲を絞り込めば、答えが出ます。このように徐々に範囲を1/2以下にする手法を2分探索といいます。
2分探索の計算量はO(log(L))なので、
N個の切れ目について全探索を行っても
O(N*log(L)) = 10**5 x 29.90・・・
            <= 10**7
なので、計算することが可能です。
"""