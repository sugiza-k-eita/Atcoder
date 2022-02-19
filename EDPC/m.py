import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

"""
二次元dp+累積和
方針

一つ前の累積和を作成
その後、現地点のdpを作成

"""
N,K = MI()
ns = LI()
ns = [0] + ns
dp = [[0]*(K+1) for i in range(N+1)]
dp[0][0] = 1
mod = 10**9 + 7
for i in range(1,N+1):
    ruiseki = [0]
    s = 0
    #最初からn地点まで参照するときに始点が0でないとだめ
    for j in range(K+1):
        s += dp[i-1][j]
        ruiseki.append(s)
    
    for j in range(K+1):
        k = max(0,j-ns[i])
        #
        dp[i][j] = ruiseki[j+1]-ruiseki[k]
        #j+1しているのは、ruisekiが0を足したK+2の長さだから
        dp[i][j] %= mod


# for xx in dp:
#     print(xx)
print(dp[-1][-1])