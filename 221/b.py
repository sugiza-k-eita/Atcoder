S = str(input())
T = str(input())
flg = 0
box = []

for i in range(len(S)-1):
    if S[i] == T[i]:
        flg = 0
        continue
    elif len(box) == 0:
        box.append([S[i], T[i]])
        flg = 1
    elif flg == 1:
        if S[i] == box[0][1] and T[i] == box[0][0]:
            flg += 1
            continue
        else:
            print("No")
            exit()
    else:
        print("No")
        exit()
print("Yes")

N = str(input())
box = []
for i in N:
    box.append(i)
box.sort()
aaa = box.pop(0)
a = []
b = []
flg = 1
for i in box:
    if flg == 1:
        a.append(i)
        flg *= -1
    else:
        b.append(i)
        flg *= -1
a.reverse()
b.reverse()
A = "".join(a)
B = "".join(b)

if A > B:
    B = B+aaa
else:
    A = A+aaa
A = int(A)
B = int(B)


print(A*B)