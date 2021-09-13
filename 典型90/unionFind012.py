# # 第12問:緑diff O(HW + Qzα(HW)) # zは配位数
# unionfinde法は連結判定の時利用する
# グラフ上の2頂点がつながっているかの判定を高速で行うことができる

class UnionFind:
    def __init__(self, n):  # O(n)
        # parent[i]にはi番目のノードの親の番号を格納し，
        # 自分が根だった場合は-(自分が属する連結集合のサイズ)とする
        self.parent = [-1 for _ in range(n)]
        self.n = n

    def root(self, x):  # 要素xの根の番号を返す O(α(n))
        if self.parent[x] < 0:  # 自分が根のとき
            return x
        else:
            # 要素xの親を要素xの根に付け替えることで次の呼び出しの高速化
            # 要素xの親を要素xの根に変えておく(付け替える)
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def size(self, x):  # 要素xの所属するグループの要素数を調べる O(α(n))
        return -self.parent[self.root(x)]  # 根のparentにサイズが格納されている

    def merge(self, x, y):  # xとyを結合する O(α(n))
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:  # 大きい方(x)に小さい方(y)をぶら下げる
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True

    def issame(self, x, y):  # xとyが同じグループにあるならTrue O(α(n))
        return self.root(x) == self.root(y)


H, W = map(int, input().split())
Q = int(input())
S = [[0]*W for _ in range(H)]
U = UnionFind(H*W+2)
# ↑わからん
dire = ((0, -1), (-1, 0), (1, 0), (0, 1))
# 塗られていないところを0 塗られたところを1とする
for _ in range(Q):
    t, *s = map(int, input().split())
    # *s はlist型
    if t == 1:
        x, y = s
        x -= 1
        y -= 1
        # 通し番号をそろえるために-1
        S[x][y] = 1
        for dx, dy in dire:
            nx, ny = x+dx, y+dy
            # 塗った場所から前後左右を調べている
            if 0 <= nx < H and 0 <= ny < W and S[nx][ny] == 1:
                # 塗った場所の前後が0より大きくHより小さい→ちゃんと範囲内に収まっているか　を調べている
                # 塗った場所の左右が0より大きくWより小さい→ちゃんと範囲内に収まっているか　を調べている
                # そこが1(赤く塗られているか)になっているか　を調べている
                U.merge((x)*(W)+y+1, (nx)*(W)+ny+1)
                # 上記の条件のとき、結合（正確に言うと大きいほうに小さいほうをくっつける）
    else:
        xa, ya, xb, yb = s
        if S[xa-1][ya-1] == 1 and S[xb-1][yb-1] == 1 and U.issame((xa-1)*(W)+ya, (xb-1)*(W)+yb):
            # S[xa-1][ya-1]が1かつ、 S[xb-1][yb-1]が1かつ、　その二つが親子関係の場合
            print('Yes')
        else:
            print('No')
