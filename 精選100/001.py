from itertools import combinations
while True:
    box = []
    cnt = 0
    N, X = map(int, input().split())
    if N == 0 and X == 0:
        break
    for i in range(1, N+1):
        box.append(i)
    for j in combinations(box, 3):
        if sum(j) == X:
            cnt += 1
    print(cnt)
