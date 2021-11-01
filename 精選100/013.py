from itertools import product, repeat
R, C = map(int, input().split())
box = []
for i in range(R):
    tmp = list(map(int, input().split()))
    box.append(tmp)
ans = 0

for bit in product((True, False), repeat=R):
    tmpbox = box
    cnt = 0
    for j in range(R):
        if bit[j]:
            for k in range(C):
                if tmpbox[j][k] == 1:
                    tmpbox[j][k] = 0
                else:
                    tmpbox[j][k] = 1
    if C != 1:
        T_box = list(zip(*tmpbox))
        for x in range(C):
            cnt += max(sum(T_box[x]), (R-sum(T_box[x])))
    else:
        cnt = sum(tmpbox)
    ans = max(ans, cnt)

print(ans)
