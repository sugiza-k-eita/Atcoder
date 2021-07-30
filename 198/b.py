n = str(input())

count = -1
for i in range(len(n)):
    if n[count] == "0":
        n = "0" + n
        count -= 1
    else:
        break
leng = len(n)//2
p = -1
flg = 0

for i in range(leng):
    if n[i] == n[p]:
        p -= 1
        continue
    else:
        flg = 1
        break

if flg == 1:
    print("No")
else:
    print("Yes")
