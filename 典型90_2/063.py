"""
問題文 
縦 H 行、横 W 列のグリッドがあり、上から i 行目、左から j 列目のマスを (i,j) で表します。マス (i,j) には整数 P i,j ​ が書かれています。 さて、このグリッドから（連続するとは限らない） 1 つ以上の行と 1 つ以上の列を選ぶことでできる「部分グリッド」であって、次の条件を満たすものを良い部分グリッドと呼びます。 条件　選んだ行を i 1 ​ ,i 2 ​ ,…,i A ​ (1≤i 1 ​ <i 2 ​ <⋯<i A ​ ≤H) とし、選んだ列を j 1 ​ ,j 2 ​ ,…,j B ​ (1≤j 1 ​ <j 2 ​ <⋯<j B ​ ≤W) とすると、マス (i a ​ ,j b ​ ) (1≤a≤A,1≤b≤B) に書かれている整数はすべて同じである。 良い部分グリッドの大きさとしてあり得る最大値を求めてください。 ただし A 個の行・ B 個の列からなる部分グリッドの大きさは A×B であるとします。
"""
# bit全探索
import itertools

H, W = map(int, input().split())

box = []
for i in range(H):
    P = list(map(int, input().split()))
    box.append(P)

ans = 0

# 行の組み合わせを全探索
for bit in itertools.product([0, 1], repeat=H):
    use_num = [i for i in range(H) if bit[i] == 1]

    # 選択された行がない場合はスキップ
    if not use_num:
        continue

    count = {}
    # 列に関しても同様に全探索
    for j in range(W):
        # 最初の行のj列目の値を取得
        value = box[use_num[0]][j]
        # すべての行でj列目の値が同じかどうかを判定
        if all(box[u][j] == value for u in use_num):
            if value not in count:
                count[value] = 1
            else:
                count[value] += 1
    freq_max = 0
    for key in count:
        freq_max = max(freq_max, count[key])

    # 選択した行の数と、すべての値が同じであった列の数を掛け合わせて部分グリッドの大きさを計算
    ans = max(ans, len(use_num) * freq_max)

print(ans)

"""
・盛り込みたい内容
Hが小さいので、Hについてbit探索が行えそう
行の組み合わせについてbit全探索を行い、その中で選択した行の数とすべての値が同じであった列の数の積が部分グリッドの大きさ

"""