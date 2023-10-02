"""
問題文 ABC 王国は H 行 W 列のマス目であらわされます。各マスは山のマスと平野のマスのどちらかです。上から i 行目、左から j 列目にあるマスが山のマスなら c i,j ​ は # 、平野のマスなら c i,j ​ は . です。 あなたは鉄道路線を作りたいです。鉄道路線の経路は、以下の条件をすべて満たす必要があります。 条件1　あるマスを始点とし、辺を共有して隣接するマスに移動することを k 回 (3≤k) 繰り返し、始点で終わる経路である。 条件2 k 回の移動について、移動先は相異なる。（始点と終点は一致してよい） 条件3　山のマスを通らない。
"""

H,W = map(int, input().split())

grid = []
for i in range(H):
    w = input()
    grid.append(w)


move_x = [-1,0,1,0]
move_y = [0,1,0,-1]
ans = -1
seen = [[False] * W for _ in range(H)]

def dfs(start, now, seen,dist=0):
    now_x, now_y = now
    # 各方向に対してDFSを進めていきます
    for i in range(4):
        nx_x, nx_y = now_x + move_x[i], now_y + move_y[i]
        if 0 <= nx_x < H and 0 <= nx_y < W and grid[nx_x][nx_y] == ".":
            if (nx_x, nx_y) == start and dist > 2:  # スタート地点に戻ってきたら
                global ans
                ans = max(ans, dist+1)  # 現在のパスの長さを計算してansを更新
            elif not seen[nx_x][nx_y]:  # 未訪問のマスがあれば
                seen[nx_x][nx_y] = True  # 訪れたとマークして
                dfs(start, (nx_x, nx_y), seen,dist+1)  # DFSを続けます
                seen[nx_x][nx_y] = False  # バックトラックします

# 各点からのDFS探索を行います
for i in range(H):
    for j in range(W):
        # 山のマスはスキップします
        if grid[i][j] == "#":
            continue
        seen = [[False] * W for _ in range(H)]  # 訪れたマスを管理するリストを初期化
        seen[i][j] = True  # スタート地点は訪れたとしてマーク
        dfs((i, j), (i, j), seen)  # DFSを開始します

print(ans)  # 最終的な答えを出力します


"""
最短経路ではなく、最長経路を求める問題
ですが、基本は最短経路のときと同じように深さ優先探索で解く。

今回、start位置が決められていませんが、gridが16マス以下なので、すべてのマスをstart位置として全探索することが可能です。

現在地から移動できるのは、上下左右の4通り

"""