import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
# def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
box = [[]]#1-indexにするためにからのリストを追加しておく
for i in range(N-1):
    C,S,F = MI()#C秒でi+1駅に行く、S秒目で最速出発し、それ以降はF秒ごとに出発
    box.append([C,S,F])

def cal(ind,now):#ind 何番目の都市か、 now 現在時刻
    C = box[ind][0]
    S = box[ind][1]
    F = box[ind][2]
    cnt = 0
    if now <= S:#もし現在時刻が、S秒以下ならS秒発の電車にのるのが最速
        now = S
    else:#すでにs秒発の電車が出発してしまっていたら、
        while S+F*cnt < now:#それから何本後の電車なら乗れるか計算する
            cnt+=1
        now = S+F*cnt#始発からcnt本後の電車に乗って次の都市に行く
    nxt =now + C#次の都市につく時間は、i番目の都市で電車に乗った時間+電車に乗ってる時間
    if ind < N-1:#次の都市でも同じように探索
        cal(ind+1,nxt)
    elif ind == N-1:#N-1番目の都市の次の都市がN番目の都市だから
        print(nxt)
    


for x in range(1,N-1):
    cal(x,box[x][1])
print(box[-1][0]+box[-1][1])
print(0)


"""
1番目の都市からN番目の都市にいくには、N-1回電車に乗れば良いです。
2番目の都市からN番目の都市にいくには、N-2回電車に乗れば良いです。
つまり、N回の操作で、最大N-1回、最小で0回の移動をするので、合計の計算量は、O(N*(N-1+0)//2)です。
今回、Nの制約が<500なので、愚直に探索しても間に合います。

今回、i番目の都市からN番目の都市に行くまでに考えなきゃいけない情報は
今到着したのが、何番目の都市なのか
到着したときの時刻はいつなのか
の2つの情報のみです。

なので、それら2つの情報を受け渡せるような再帰の関数を書いてあげれば良いです。
とはいえ、再帰の関数は書くのが難しいと思いますので、なにか伝わりづらいところがあればここまで連絡ください！！
"""