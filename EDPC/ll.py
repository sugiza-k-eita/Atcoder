import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
"""
奇数のときは、最大値、偶数のときは最小値
埋める順番は、wが小さい順

"""
N = II()
ns = LI()

dp = [[0]*(N+1) for i in range(N+1)]

for w in range(1,N+1):
    for l in range(N-w+1):
        r = l + w
        if w % 2 == N%2:#これで先行後攻がわかる
            dp[l][r] = max(dp[l+1][r] + ns[l], dp[l][r-1] + ns[r-1])
            #先頭から取るか、末尾からとるかの2択
            #先頭から取る場合は、ns[l]、l+1~rまでの最大値、の合計で求まる
        else:
            dp[l][r] = min(dp[l+1][r] + ns[l], dp[l][r-1] + ns[r-1])
            #先頭から取るか、末尾からとるかの2択
            
for xx in dp:
    print(xx)
