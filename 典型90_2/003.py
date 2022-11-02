from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()

node = [[] for i in range(N)]
for i in range(N-1):
    a,b = MI()
    a -= 1#0始まりにするために-1
    b -= 1
    node[a].append(b)
    node[b].append(a)

seen = [0]*N#flg

def dfs(u):
    for v in node[u]:#node[u]から行ける都市
        if seen[v] == 0:#その都市にまだ訪れたことがなければ
            seen[v] = seen[u]+1
            dfs(v)
            
dfs(0)#任意の都市からの最長距離である都市iを求める 
max_index = seen.index(max(seen))


seen = [0]*N
dfs(max_index)#都市iからの最長距離である都市jを求める
ans = (max(seen))#木の直径(i→j)
print(ans+1) # (j→i)に戻る必要があるので、+1

"""
003 - Longest Circular Road（★4）
https://atcoder.jp/contests/typical90/tasks/typical90_c

今回の問題は、「一筆書きでどれだけ遠くに行けるかが知りたい」という最長距離を求める問題に読み替えることできます。
なぜなら、「どの都市の間も、いくつかの道路を通って移動可能なもの」であるため、始点の都市から終点の都市までできる限り遠回りしていき、「新設する道路」を始点↔終点に設ければ良いからです。
今回の問題はグラフの問題でかつ、一筆書きなので、dfsで実装すれば解けそうです。


では、どこを始点として、どこを終点とするか？
では、始点と終点をどこにすれば、最長距離になるのでしょうか？
例えば、始点を0からNの間を全探索して、dfsを実装すれば解けそうです。
しかし、今回、N < 10**5　なので、始点について全探索してしまうと、
始点の全探索O(10**5) x 1操作あたりのdfsの計算量O(10**5)かかってしまい、TLEしてしまいます。
なので、始点と終点を求めるのにすこし工夫が必要です。

木の直径を考える
このように2点間の最長距離を求めることを木の直径を求めるといいます。
求め方は、
任意の点からdfsを行う(得られた最長距離の点をiとする)
点iからdfsを行う(得られた最長距離の点をjとする)
今回の木の直径は(i,j)となる

余談　なぜそうなるの？
詳しくはの記事
https://algo-logic.info/tree-diameter/
や「木の直径　証明」などと調べると出てきますが、ちょっとだけ解説すると
任意の都市からもとめた最長距離であるiという都市は、その木構造において必ずどこかの葉の末端になります。
なので、iという葉の末端にあたる都市から、一番遠いjという別の葉の末端までの距離が最長距離となるわけです。
(違ったらごめんなさい)

「木の直径」っていう考え方は、この問題を通して初めて知りました。



"""