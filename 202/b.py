s = str(input())
split_s = []
for i in range(len(s)):
    split_s.append(int(s[i]))
split_s.reverse()
ans = []
for i in split_s:
    if i == 6:
        i = 9
        ans.append(i)
    elif i == 9:
        i = 6
        ans.append(i)
    else:
        ans.append(i)

print(*ans, sep="")
