#https://atcoder.jp/contests/abc180/tasks/abc180_e
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

"""
bitDP
dp[s][v] = 今まで訪れた頂点集合がSで、今いる頂点がVのときの最小のコスト
v→uの時
dp[s+u][u],dp[s][v]+dist[v][u]
"""


N = int(input())
G = [[float("inf")] * N for _ in range(N)]  # # 存在しないパスはinfになるように、最初にすべてinfにしておく
P = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        G[i][j] = (
            abs(P[i][0] - P[j][0]) + abs(P[i][1] - P[j][1]) + max(0, P[i][2] - P[j][2])
            #cost　これは問題によって異なるから注意
        )

# dp[S][t]: 集合Sにおいてtが末項となる際の最小コスト
dp = [[float("inf")] * N for _ in range(2**N)]
dp[0][0] = 0  # 出発地点初期化

# 配るDPで実装
for S in range(2**N):  # 集合をbitで管理
    for v in range(N):  # もらう側
        for u in range(N):  # 配る側
            # uが到達済みでない場合continue
            if not (S >> u) & 1 and S != 0:
                #Sがu(配る側)に到達していなくて、その点が0ではない時は、配ることができないので
                continue
            # vが未訪問である場合: 距離を
            if (S >> v) & 1 == 0:
                if dp[S][u] + G[u][v] < dp[S | (1 << v)][v]:
                    dp[S | (1 << v)][v] = dp[S][u] + G[u][v]
# 集合"1" * Nにおいて末項が0となる場合の最小コスト
print(dp[(1 << N) - 1][0])