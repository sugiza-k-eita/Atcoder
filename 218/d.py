from collections import defaultdict


N = int(input())
xy = []
for i in range(N):
    a, b = map(int, input().split())
    xy.append([a, b])

dic = defaultdict(int)
for i, j in xy:
    dic[(i, j)] = dic[(i, j)] + 1
    # i,j==0,0のとき　dic(0,0) =0に+1している

ans = 0
for i in range(N-1):
    for j in range(i+1, N):
        x1, y1 = xy[i]
        # 左下
        x2, y2 = xy[j]
        # 右上
        if x1 != x2 and y1 != y2 and dic[(x1, y2)] > 0 and dic[(x2, y1)] > 0:
            # x座標が異なっていて、かつ、y座標も異なっていて,　→一直線上にないことの証明
            # x1,y2があり、x2,y1がdicに含まれる場合
            # →左上と右下の座標がそれぞれdictに含まれる場合
            ans += 1
print(ans//2)
# 右下と左上の2通りを数えてしまっているから、//2
