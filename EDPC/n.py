import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

"""
区間DPと累積和累積和を使う問題

典型的な区間 DP の問題ですね。

dpl,r=dpl,r= ( 区間 [l,r][l,r] を 11 匹のスライムにするために必要なコストの最小値 ) 
という DP を行えばいいです。
区間 [l,r][l,r] になる直前にどこで切れていたかをすべて試すと
遷移が O(N)O(N) でできるので、全体で O(N3)O(N3) となり、解けます。


"""
N = II()
ns = LI()
dp=[[10**18+7]*(N) for i in range(N)]
#はじめの状態の累積和を作成
#累積和の長さは、(N+1)+1
for i  in range(N):
    dp[i][i] = 0
ruiseki = [0]
s = 0
for i in range(N):
    s += ns[i]
    ruiseki.append(s)

for w in range(1, N):
    #wを設定　幅が0のときは区間がないので0のまま
    for l in range(N-w):
        r = l+w
        i_sum = ruiseki[r+1] - ruiseki[l]
        #l~rまでの区間で合成にかかったコスト これは合成の順番関わらず、最後の２つを合成するときにかかるコストである
        for k in range(w):
            dp[l][r] = min(dp[l][r], dp[l][l+k] + dp[l+k+1][r] + i_sum)
            #l~k間で出来るスライムとk+1~rで出来るスライムがあり、その２つのスライムの合計(i_sum)


# for xx in dp:
#     print(xx)
print(dp[0][-1])