import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

H,W = MI()
H_box = []
W_box = []
box = []
for i in range(H):
    A = LI()
    box.append(A)
    H_box.append(sum(A))

box_t = [list(x) for x in zip(*box)]

for i in range(W):
    W_box.append(sum(box_t[i]))

ans_box = [[] for i in range(H)]
for i in range(H):
    for j in range(W):
        ans = H_box[i]+W_box[j]-box[i][j]
        ans_box[i].append(ans)

for x in range(H):
    print(*ans_box[x],sep=" ")

"""
004 - Cross Sum（★2）
https://atcoder.jp/contests/typical90/tasks/typical90_d

例えば、
i行目、j列に出力される値は、
i行目の合計+j列目の合計-i行目j列目の数字
となります。
(i行目j列目の数字のみ、i行目の合計としてもj列目の合計としても2回加算されているため)

なので
行方向の合計を取る
列方向の合計を取る(今回は転置して、列→行にしてから求めています)
すべてのi行目j列目のマスにおいて、i行目の合計+j列目の合計-i行目j列目の数字を出力する
で答えが得られます。
"""