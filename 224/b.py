from itertools import combinations
H, W = map(int, input().split())
box = []
for i in range(H):
    table = list(map(int, input().split()))
    box.append(table)
for a in combinations(range(H), 2):
    i1, i2 = a[0], a[1]
    for b in combinations(range(W), 2):
        j1, j2 = b[0], b[1]
        left = box[i1][j1] + box[i2][j2]
        right = box[i2][j1] + box[i1][j2]
        if left <= right:
            continue
        else:
            print("No")
            exit()

print("Yes")
