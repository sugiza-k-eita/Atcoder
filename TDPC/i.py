import sys, math
sys.setrecursionlimit(1000000)
INF = 1 << 100
#mod = 1000000007
mod = 998244353
input = lambda: sys.stdin.readline().rstrip()
li = lambda: list(map(int, input().split()))

S = input()
N = len(S)

dp = [[0] * N for _ in range(N)]#l以上r以下で何文字削除できるかをdp
for i in range(3, N+1):
    #i 幅
    for L in range(N):
        R = L + i - 1
        #L以上R以下で削除できる文字が何文字あるかを考える
        if R >= N:
            break
        #RがN以上なら、dpの範囲外になっちゃうからbreak
        if i == 3 and S[L:R+1] == 'iwi':
            #文字列の参照規則により、s[x:y]はxからy未満をみる
            #そのため、今回はs[l:r+1]としてr+1未満→r以下と解釈できる
            dp[L][R] = max(dp[L][R], 3)
        for mid in range(L, R):
            if S[mid] == 'w' and S[L] == S[R] == 'i':
                #両端がiでどこかのwで消す場合は、l-mid間とmid+1-rの文字をすべて消せるならいける
                if (mid - 1 - L == dp[L][mid-1]) and (R - mid - 1 == dp[mid+1][R]):
                    #mid - 1 - L 、R - mid - 1 は文字の長さ　
                    # 文字の長さ＝＝消せる文字の長さならl+1～r-1間はすべて消せて、l,mid,rで削除できる
                    dp[L][R] = max(dp[L][R], dp[L+1][mid-1] + dp[mid+1][R-1] + 3)
            dp[L][R] = max(dp[L][R], dp[L][mid] + dp[mid+1][R])
            #iwiiwiみたいな文字列の場合は、iwi iwiで区切って削除したほうが良い

for xx in dp:
    print(xx)
# print(dp[0][N-1] // 3)
