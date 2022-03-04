import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()
INF = float("inf")
dp = [[INF]*N for i in range(N)]


for i in range(N):
    dp[i][i] = 0
ruiseki = [0]
s = 0
for i in range(N):
    s += A[i]
    ruiseki.append(s)


for w in range(1,N):
    for l in range(N):
        r = l + w
        if r >= N:
            continue
        i_sum = ruiseki[r+1] - ruiseki[l]
                #l~rまでの区間で合成にかかったコスト これは合成の順番関わらず、最後の２つを合成するときにかかるコストである
        # dp[l][r] = min(A[l] + A[r],dp[l][r])
        for mid in range(l,r):
            dp[l][r] = min(dp[l][r], dp[l][mid]+dp[mid+1][r]+i_sum)

# for xx in dp:
#     print(xx)

print(dp[0][-1])