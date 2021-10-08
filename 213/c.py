H, W, N = map(int, input().split())
R = []
C = []

for _ in range(N):
    r, c = map(int, input().split())
    R.append(r)
    C.append(c)

Rs = sorted(set(R))  # `set`で重複を省いてソートしたリスト`Rs`
Cs = sorted(set(C))

# Rd = {Rs[i]: i+1 for i in range(len(Rs))} と同じです
Rd = {x: i for i, x in enumerate(Rs, 1)}
# 圧縮した際に行番号の再連番
# 3:1 だったら3→1になるよーっていう意味
print(Rd)
Cd = {x: i for i, x in enumerate(Cs, 1)}
# 圧縮した際に列番号の再連番

print(R)
print(C)
for r, c in zip(R, C):
    # zipは複数のリストの内容を展開
    print(Rd[r], Cd[c])
