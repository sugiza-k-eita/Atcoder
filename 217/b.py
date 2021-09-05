box = ["ABC", "ARC", "AGC", "AHC"]
s1 = input()
s2 = input()
s3 = input()
flg = []
for i in range(4):
    if s1 == box[i]:
        flg.append(i)
    elif s2 == box[i]:
        flg.append(i)
    elif s3 == box[i]:
        flg.append(i)


flg.sort()
flg.reverse()

for i in flg:
    box.pop(i)

print(*box, sep="")
