import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import itertools

N = II()
d = {}
d[-1] = "("
d[1] = ")"
for bits in itertools.product([-1,1],repeat=N):
    if sum(bits) != 0:
        continue
    tmp = 0
    flg = True
    for i in bits:
        tmp += i
        if tmp == 1:
            flg = False
            break
    if flg:
        ans = ""
        for j in bits:
            ans += d[j]
        print(ans)
        
        
    

        

"""
制約に注目
今回Nの制約が20以下です。こーゆー時はbit探索です。
bit探索とは
計算量が2**N
0 or 1　のようにフラグの働きをもつ問題のときに使える
大抵、制約が20 or 16以下のときに使うことが多いイメージ

今回の問題は長さNの( or )のどちらかを取る文字列です。
そこで、
( = -1 
) = 1
として、
前から文字列を見て、数字を加算して行ったときに、プラスになったらそれは文字列の並びとして正しくないといえます
ex
())(
-1,1,1,-1 で表せる
前から加算をしていくと、3回目の操作のときで、プラスになる。
これは、文字列として正しくない。

なので、bit全探索をして、出てきた数列を前から見ていったときに、最後まで条件を満たせば出力します。
bit全探索には、itertoolsのproductを使うと、楽に実装できます。

"""