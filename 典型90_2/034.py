
import collections 
N,K = map(int, input().split())
A = list(map(int, input().split()))
cnt = collections.defaultdict(int)
for i in range(K):
    cnt[A[i]] += 1#[0,K)の中に何種類の数字があるかカウント

r = K
l = 0
ans = 0
for r in range(K,N):#rの取りうる範囲である[K,N)まで探索
    cnt[A[r]]+=1#A[r]のカウント+1
    while len(cnt) > K and l < N-K:#もしK種類よりも多い数字がカウントされたら範囲を狭める必要がある
        # print(len(cnt),l,r)
        cnt[A[l]] -=1#A[l]のカウント-1し
        if cnt[A[l]] == 0:#もし、A[l]のカウントが0になったら
            del cnt[A[l]]#cntからA[l]を消去し、cntの長さを短くする
        l += 1#lを一つ右に動かす
    ans = max(ans,r-l+1)#連続する部分列の最大値を記憶

print(ans)

"""
今回は、任意のLとRを決めた際に、[L,R)に含まれる数字の種類を最大にする問題です。
愚直にL,Rについて[0,N)を探索してしまうと、TLEになってしまいます。
※N≤100,000のため、O(N^2)はTLEする

ここで、注目したいのは、RはLよりも右側になければならないということです
(L,Rなので当たり前のようですが重要です)
つまり、左端から探索を始めた場合、
任意の[L,R)区間において、K種類以下ならRを右にやり範囲を広げ、K種類以上なら、Lを右にやり範囲狭める
ことですべての範囲について探索できます。
このように任意の区間をO(2N)で解く方法を尺取法といいます
(違ったらすみません)
そのため、今回は尺取法を用いて、L,Rについて探索を行えば解けます。


累積和と尺取法をマスターしたい

"""