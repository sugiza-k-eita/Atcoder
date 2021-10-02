N = int(input())
X, Y = map(int, input().split())
INF = 1000
dp = [[[INF]*(Y+1) for i in range(X+1)] for i in range(N+1)]
box = []
for i in range(N):
    a, b = map(int, input().split())
    box.append((a, b))

# 3次元dp
# 今回はdp[0][0][0](なにも選ばない状態)を0としてそれ以外を無限とする
dp[0][0][0] = 0

for i in range(N):
    a, b = box[i]
    for j in range(X+1):
        minj = min(j + a, X)
        # X個以上のたこ焼きを食べる場合はXを利用すればよい
        # なぜならX個以上食べる場合はすべて条件を満たしているため、最小で超えることのできるXのときの値を使用すればよいため
        for k in range(Y+1):
            mink = min(k+b, Y)
            # Y個以上のたい焼きを食べる場合はYを利用すればよい
            # なぜならY個以上食べる場合はすべて条件を満たしているため、最小で超えることのできるYのときの値を使用すればよいため
            dp[i+1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])
            # dpの更新
            dp[i + 1][minj][mink] = min(dp[i + 1][minj][mink], dp[i][j][k] + 1)
            # 最小で超える時の更新


if dp[N][X][Y] == INF:
    print(-1)
else:
    print(dp[N][X][Y])
