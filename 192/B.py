S = input()
Odd = []
Even = []
upper_list = ["Q", "A", "Z", "W", "S", "X", "E", "D", "C", "R", "F", "V",
              "T", "G", "B", "Y", "H", "N", "U", "J", "M", "I", "K", "O", "L", "P"]
tmp_lower_list = ["Q", "A", "Z", "W", "S", "X", "E", "D", "C", "R", "F",
                  "V", "T", "G", "B", "Y", "H", "N", "U", "J", "M", "I", "K", "O", "L", "P"]
lower_list = []
for i in range(26):
    tmp = tmp_lower_list[i].lower()
    lower_list.append(tmp)

for i in range(len(S)):
    if i % 2 == 0:
        Odd.append(S[i])
    else:
        Even.append(S[i])

flg = 0
for i in Odd:
    if i in lower_list:
        continue
    else:
        flg += 1
        break
for i in Even:
    if i in upper_list:
        continue
    else:
        flg += 1
        break

if flg == 0:
    print("Yes")
else:
    print("No")
