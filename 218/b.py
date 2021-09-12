s = list(map(int, input().split()))
cnt = "0abcdefghijklmnopqrstuvwxyz"
ans = []

for i in s:
    ans.append(cnt[i])

print(*ans, sep="")
