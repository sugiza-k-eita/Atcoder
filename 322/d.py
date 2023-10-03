import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)
from itertools import product

# 各ポリオミノを90度回転させる関数
def rotate(poli):
    return [''.join(poli[3-j][i] for j in range(4)) for i in range(4)]

# 各ポリオミノを(dx, dy)だけ平行移動させる関数
def move(poli, dx, dy):
    return [''.join(poli[i-dx][j-dy] if 0 <= i-dx < 4 and 0 <= j-dy < 4 else '.' for j in range(4)) for i in range(4)]

# ２つのフィールドが重なっていないかチェックする関数
def check(field1, field2):
    return all(field1[i][j] == '.' or field2[i][j] == '.' for i in range(4) for j in range(4))

# ３つのポリオミノを組み合わせて4x4のフィールドを埋めることができるか調べる関数
def solve(polios):
    for perms in product(range(4), repeat=3):
        for dxs, dys in product(product(range(4), repeat=2), repeat=3):
            # 各ポリオミノを回転・平行移動させる
            moved = [ [move(rotate(polios[i], r), dx, dy) for r in range(4)] for i, (dx, dy) in enumerate(zip(dxs, dys))]
            
            # 全ての組み合わせに対して試す
            for poli_comb in product(*moved):
                final_field = [['#' if any(poli[i][j] == '#' for poli in poli_comb) else '.' for j in range(4)] for i in range(4)]
                
                # final_fieldが全て#で埋まっているかチェック
                if all(final_field[i][j] == '#' for i in range(4) for j in range(4)):
                    return True
    return False

# 主処理
polios = [ [input().strip() for _ in range(4)] for _ in range(3)]
print("Yes" if solve(polios) else "No")
