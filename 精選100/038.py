import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
for x in range(N):
    s = S()
    t = S()
    s = "_"+s
    t = "*"+t
    leng_s = len(s)
    leng_t = len(t)

    dp= [[0]*leng_s for i in range(leng_t)]

    for i in range(1,leng_t):
        for j in range(leng_s):
            if t[i]== s[j]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j]= max(dp[i][j-1],dp[i-1][j])
    print(dp[-1][-1])