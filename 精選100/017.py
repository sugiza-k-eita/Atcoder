from itertools import permutations

N = 8

M = [['.']*N for i in range(N)]
A0 = set()  # 右斜め上
B0 = set()  # 右斜め下

K = int(input())
R = set(range(N))  # Row
C = set(range(N))  # Col
for i in range(K):
    r, c = map(int, input().split())
    R.remove(r)
    C.remove(c)
    M[r][c] = 'Q'
    A0.add(r+c)
    B0.add(r-c)

for per in permutations(C):
    A = A0.copy()
    B = B0.copy()
    flg = True
    for r, c in zip(R, per):
        if r+c in A:
            flg = False
        A.add(r+c)
        if r-c in B:
            flg = False
        B.add(r-c)
    if flg:
        for r, c in zip(R, per):
            M[r][c] = "Q"
    if flg:
        break
print(*("".join(m) for m in M), sep='\n')
