# pypyだと通らない
from itertools import combinations, product, repeat

N, M = map(int, input().split())
freindship = [[]for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    freindship[a].append(b)
    freindship[b].append(a)

ans = 1

for bit in product((0, 1), repeat=N):
    box = []
    cnt = 0
    flg = 0
    if sum(bit) <= 1:
        continue
    for i in range(N):
        if bit[i] == 1:
            box.append(i)
    for j, k in combinations(box, 2):
        if not k in freindship[j]:
            flg += 1
    if flg == 0:
        ans = max(ans, sum(bit))
        # print(box)
print(ans)
