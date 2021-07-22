N = int(input())
section = []
for i in range(N):
    t, l, r = map(int, input().split())
    if t == 2:
        r -= 0.5
    elif t == 3:
        l += 0.5
    elif t == 4:
        l += 0.5
        r -= 0.5
    section.append([l, r])
count = 0
for i in range(len(section)):
    for j in range(i+1, len(section)):
        if section[i][0] > section[j][1] or section[i][1] < section[j][0]:
            continue
        else:
            count += 1
print(count)
