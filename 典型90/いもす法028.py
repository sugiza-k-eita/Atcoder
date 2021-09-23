N = int(input())
H = W = 1001
# ↑lx,ly rx,ryの取りうる最大値よりも大きいxy平面を作成

rectangles = [list(map(int, input().split())) for i in range(N)]
# 1行で二次元配列を作れる

cost = [1]*N
# 重なったら+1


def imos2(H, W, rectangle, cost):  # 二次元imos法 O(N+WH)
    # lx,ly,rx,ry := rectangle[i]
    # H行W列のマスについて、ly<=y<ry,lx<=x<rxの範囲に一様にcost[i]を加算
    n = len(rectangle)
    # n==N 引数に渡すのめんどいから
    tiles = [[0]*W for y in range(H)]
    for i, (lx, ly, rx, ry) in enumerate(rectangle):
        # 左上と右下には加算、左下と右上は減算
        tiles[ly][lx] += cost[i]
        # 左上
        tiles[ry][lx] -= cost[i]
        # 右上
        tiles[ly][rx] -= cost[i]
        # 左下
        tiles[ry][rx] += cost[i]
        # 右下

    # 横方向の累積和
    for y in range(H):
        for x in range(1, W):
            tiles[y][x] += tiles[y][x-1]
    # 縦方向の累積和
    for x in range(W):
        for y in range(1, H):
            tiles[y][x] += tiles[y-1][x]
    return tiles  # List[List[int]]


tiles = imos2(H, W, rectangles, cost)
ans = [0]*(N+1)
print(tiles)
# 重なっている面積ごとの合計を出す
for i in range(H):
    for j in range(W):
        if tiles[i][j] != 0:
            ans[tiles[i][j]] += 1

print(*ans[1:], sep="\n")
