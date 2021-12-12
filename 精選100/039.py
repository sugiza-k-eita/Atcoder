import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
ns = LI()

dp = [[0]*21 for i in range(N-1)]

dp[0][ns[0]]= 1
for i in range(1,N-1):
    for j in range(21):
        if dp[i-1][j] != 0:
            plus = j + ns[i]
            minus = j - ns[i]
            if plus <= 20:
                dp[i][plus] += dp[i-1][j]
            if minus >= 0:
                dp[i][minus] += dp[i-1][j]
# for x in dp:
#     print(x)
print(dp[-1][ns[-1]])