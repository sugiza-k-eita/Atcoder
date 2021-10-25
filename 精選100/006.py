N = int(input())
S = str(input())
ans = 0

for i in range(1000):
    left = str(i//100)
    middle = str((i//10) % 10)
    right = str(i % 10)
    pw = [left, middle, right]
    cnt = 0
    for s in S:
        if s == pw[cnt]:
            if cnt < 2:
                cnt += 1
            elif cnt >= 2:
                ans += 1
                break

print(ans)
