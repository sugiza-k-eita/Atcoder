"""
bit探索だと計算量オーバーする
Nが偶数ならN//2
Nが奇数ならN//2+1が表じゃないといけない
なので、nCpで・・・
3000C1500は余裕で、10**6超えるからだめ

確率DPで解く
表が出た枚数がわかってれば大丈夫そうだから
dp[i][j]=(i枚目のコインまで投げたとき、表がj枚でる確率)
で出来そうだよ。
"""
#N < 3000　という時点で、N**2を使うんじゃねって検討をつけとくと良いかも
import sys
def LI(): return list(map(float,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
ns = LI()
dp = [[0]*(N+1) for i in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        dp[i+1][j+1] += dp[i][j]*ns[i]
        dp[i+1][j] += dp[i][j]*(1-ns[i])

# for xx in dp:
#     print(xx)

if N%2== 0:
    rep = N//2
else:
    rep = N//2 + 1
ans = 0
for i in range(rep,N+1):
    ans += dp[-1][i]
print(ans)
