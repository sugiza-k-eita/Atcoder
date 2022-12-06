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
    X,L = MI()
    head = X-L
    tail = X+L
    box.append([tail,head])

box.sort()
last_tail = box[0][0]
cnt = 1
for i in range(1,N):
    if box[i][1] < last_tail:
        continue
    last_tail = box[i][0]
    cnt += 1
print(cnt)

"""
まずはじめに、
今回、ロボットを配置するかどうかを決める際に、両腕の区間を記憶しておくのは、少しめんどいです。なのでどうにか楽をしたいのです。
そのように考えたときに、前から見ていったときに
最後に配置したロボットの正の方向に伸びる手(tail)と今から配置しようとしているロボットの負の方向に伸びる手(head)だけを見るようにすれば、
ロボットの両腕の区間を記憶する必要なく、2値の大小関係を見るだけで、大丈夫になります。

N個のロボットの手が重ならないようにしたい
つまり、ロボットを配置したときに、
「i-1番目までの操作で配置すると決めたロボットと、i番目のロボットの手が重ならないようにしたい」
わけです。

繰り返しになりますが、上記の操作に関しては、i回目の操作に関しては、見るべき情報は
i-1番目までの操作で最後に配置すると決めたロボットのtail
i番目のロボットのhead
の2つの要素だけです。
※head = X-L, tail = X+L

貪欲法の説明
このように、i回目の操作において、

手順
そのため、tailの小さい順に見ていき、
i番目の操作において
「i-1番目までの操作で最後に配置すると決めたロボットのtail」よりもi番目のロボットのheadが大きければ(重なっていなければ)配置
重なっている場合は、配置しない

とします。
"""
