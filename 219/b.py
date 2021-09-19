S1 = input()
S2 = input()
S3 = input()
T = str(input())

ans = []
for i in T:
    if i == "1":
        ans.append(S1)
    elif i == "2":
        ans.append(S2)
    else:
        ans.append(S3)

print(*ans, sep="")
