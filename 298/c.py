import bisect
#bisectは既に整列されている配列に対して高速で挿入できるライブラリ
#今回は昇順で(整列して)出力する必要があるため使用している

N = int(input())
#query2用のリスト
box = [[] for i in range(N+1)]#1-indexにしたいので、+1
#query3用のリスト
num_box = [[] for i in range(2*(10**5)+1)]#1-indexにしたいので、+1
Q = int(input())

for i in range(Q):
    a = list(map(int, input().split()))
    ind = a[0]
    if ind == 1:#query1なら
        i,j = a[1],a[2]
        bisect.insort(box[j],i)#j番目のboxにカードiを挿入
        bisect.insort(num_box[i],j)#j番目のカードが入っているbox[j]を記憶
    
    elif ind == 2:
        i = a[1]
        print(*box[i],sep=" ")
    
    elif ind == 3:
        i = a[1]
        ans = set(num_box[i])#重複なしで出力する必要があるためsetを使用
        print(*ans,sep=" ")

"""
python3.8だと通らないのでpypyで
C - Cards Query Problem
https://atcoder.jp/contests/abc298/tasks/abc298_c

入力
N:空の箱の長さ
Q:クエリの個数
query:3つの処理内容

query2では箱iに入っているカードについて出力し、query3では数iが書かれている箱について出力する必要があります。
そのため、どの箱にどのカードが入っているかを記憶するlistの他に、どの数がどの箱に入っているかを記憶するlistを用意する必要があります。

今回箱の個数も数の最大値も2x10^5以下なので、特別工夫することなくlistを作ることができます

"""