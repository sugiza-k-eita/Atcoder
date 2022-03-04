import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N, K =MI()
A =[0] + LI()

dp = [[0]*(K+1) for i in range(N+1)]
dp[0][0] = 1

for i in range(1,N+1):
    ruiseki = [0]
    s = 0
    #最初からn地点まで参照するときに始点が0でないとだめ
    for j in range(K+1):
        s += dp[i-1][j]
        ruiseki.append(s)

    for j in range(K+1):
        k = max(0,j-A[i])
        dp[i][j] = ruiseki[j+1]-ruiseki[k]
        dp[i][j] %= 10**9+7



# for xx in dp:
#     print(xx)
print(dp[-1][-1])