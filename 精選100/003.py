S = str(input())
cnt = 0
ans = 0
for i in S:
    if i == "A" or i == "C" or i == "G" or i == "T":
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt)
print(ans)
