from itertools import combinations

N = int(input())
box = []
for i in range(N):
    x, y = map(int, input().split())
    box.append([x, y])
cnt = 0
for a in combinations(range(N), 3):
    I = a[0]
    J = a[1]
    K = a[2]
    x_i, y_i = box[I][0], box[I][1]
    x_j, y_j = box[J][0], box[J][1]
    x_k, y_k = box[K][0], box[K][1]
    if x_i == x_j == x_k:
        continue
    if y_i == y_j == y_k:
        continue
    Ynozouka1 = (y_i-y_j)
    Xnozouka1 = (x_i - x_j)
    Ynozouka2 = (y_k-y_j)
    Xnozouka2 = (x_k - x_j)
    if Xnozouka1 == 0 or Xnozouka2 == 0:
        cnt += 1
        continue
    if Ynozouka1 == 0 or Ynozouka2 == 0:
        cnt += 1
        continue

    henka1 = Ynozouka1 / Xnozouka1
    henka2 = Ynozouka2 / Xnozouka2
    if henka1 != henka2:
        cnt += 1
print(cnt)
