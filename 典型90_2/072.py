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


