import sys

sys.setrecursionlimit(10000)


def dfs(h, w):
    lands = [list(map(int, input().split())) for _ in range(h)]
    seen = [[True]*w for _ in range(h)]

    def isin(y, x):
        return 0 <= y < h and 0 <= x < w
        # 範囲外ならだめ！

    def done(y, x):
        seen[y][x] = False
        # 一度訪れたところをFalseにする
        for i in range(-1, 2):
            for j in range(-1, 2):
                ny = y + i
                nx = x + j
                # ny,nxはlands[y][x]の上下左右の8方位を全探索している
                if isin(ny, nx) and lands[ny][nx] == 1 and seen[ny][nx]:
                    # 範囲内かつ、そこが陸地なら0k
                    done(ny, nx)
    res = 0
    for i in range(h):
        for j in range(w):
            if lands[i][j] == 1 and seen[i][j]:
                done(i, j)
                # つながっている島がなくなったら+1
                res += 1

    return res


while True:
    w, h = map(int, input().split())
    if h == 0:
        break
    print(dfs(h, w))
