N = int(input())
s = input()
t = input()

for i in range(N):
    if s[i] == t[i]:
        continue
    elif s[i] == "o" and t[i] == "0":
        continue
    elif s[i] == "0" and t[i] == "o":
        continue
    elif s[i] == "l" and t[i] == "1":
        continue
    elif s[i] == "1" and t[i] == "l":
        continue
    else:
        print("No")
        exit()
print("Yes")