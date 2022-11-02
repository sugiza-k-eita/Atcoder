import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


sx,sy,tx,ty = MI()
first_go = (tx-sx)*"R" + (ty-sy)*"U"
first_come = (tx-sx)*"L" + (ty-sy)*"D"
second_go = "D"+(tx-sx+1)*"R"+(ty-sy+1)*"U"+"L"
second_come ="U"+(tx-sx+1)*"L" + (ty-sy+1)*"D" + "R"
print(first_go+first_come+second_go+second_come)

"""
今回、操作では、初期位置(sx,sy)から目的地(tx,ty)を2回往復する問題です。
その中での制約として、同じ道を通ってはいけないが、移動回数を少なくする必要があります。
そこで今回は、
1回目の往復は最短経路
2回目の往路では、(sx,sy)→(sx,sy-1)→(tx+1,ty)→(tx,ty)→(tx,ty+1)→(sx-1,sy)と大回りの経路を通るようにします。

今回の問題で大事なのは、同じ道を通らない最短経路は2種類しかないということに気づけるかということです。
そして、その条件に気づけてたら、2回目の往復は必然的に最短経路から1マス分膨らんだところを目指す必要があります。

別アプローチ
(tx,ty)までに行き方として、(tx-1,ty),(tx,ty-1),(tx+1),(tx,ty+1)の4つの場所から移動するしかないので、逆に今回の問題ではそれらの4つの行き方を網羅する必要がある事がわかる
"""