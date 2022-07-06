import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

"""
https://atcoder.jp/contests/abc080/tasks/abc080_c
C - Shopping Street

問題文がややこしいです！！

N個の店があって、そのうち、
i番目の店は月曜日の午前中から金曜日の午後にかけて(j=1-5,k=0-1)、営業しているか(1)していないか(2)の情報が渡される

入力
F[i][j][k]　営業しているかどうかの情報
iが店番
jが曜日
kが時間

P[i][j] 店の利益
i 店番
j 営業時間がかぶっている個数

Fでのindex_jとPでのindex_jは別のものを指すので注意が必要です。
説明をわかりやすくするために、Pでのindex_jをcnt(営業時間がかぶっている回数)と言い換えて説明します。

今回行いたいのは、joisonお姉さんはどのような営業時間(0と1からなる配列)であれば、利益を最大化できるかです。
なので、joisonお姉さんの取りうる配列を全探索します。
配列は、0 or 1　からなる長さ10のはいれつなので、bit全探索を行います。
bit全探索は、O(2^10)ですので、今回は十分に間に合います。
手順
bit全探索を用いてjoisonお姉さんの営業時間を表す配列を作成
    作成された配列に対し、既存の店(i)と営業時間が何回かぶっているか記録(cnt)し、
    その後、配列Pを用いて、i番目の店から得られる利益を求めます。
    上記操作をすべての店で行い、その配列のときの利益を確定
得られた利益の内、最大値を出力
"""

from itertools import product
N = II()
F = []
for i in range(N):
    A = LI()
    F.append(A)


#営業するときの利益
P = []
for i in range(N):
    B = LI()
    P.append(B)
    
ans = -10**18
#初期値
for bits in product([0, 1], repeat=10):
    tmp_ans = 0
    if sum(bits) == 0:
        continue
    
    for i in range(N):
        cnt = 0#営業時間がかぶっている回数を記録
        for j in range(10):
            if bits[j] ==1 and F[i][j] == 1:
                #両方営業しているなら
                cnt += 1
        #i番目の店はcnt回営業時間がかぶっている
        tmp_ans += P[i][cnt]
    #すべての店で、得られた利益(tmp_ans)とこれまでの最大値(ans)を比較
    ans = max(ans,tmp_ans)
                
print(ans)
    