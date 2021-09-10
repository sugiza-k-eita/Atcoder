H, W = map(int, input().split())
box = [[] for i in range(H)]
for i in range(H):
    box[i] = list(map(int, input().split()))

H_ans = [0 for i in range(W)]
W_ans = [0 for i in range(H)]

for i in range(H):
    W_ans[i] = sum(box[i])
    for j in range(W):
        H_ans[j] += box[i][j]

ans_box = [[[] for i in range(W)] for j in range(H)]
for i in range(H):
    for j in range(W):
        ans_box[i][j] = H_ans[j]+W_ans[i]-box[i][j]
    print(*ans_box[i], sep=" ")
