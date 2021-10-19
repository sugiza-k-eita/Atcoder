N = int(input())

cnt = [0]*(N+1)
ans = 0
for i in range(1, (N+1), 2):
    for j in range(1, i+1):
        if i % j == 0:
            cnt[i] += 1
for i in cnt:
    if i == 8:
        ans += 1
# print(cnt)

print(ans)
