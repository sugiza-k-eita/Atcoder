N = int(input())
letter = input()

t_cnt = 0
a_cnt = 0
last = ""
for i in range(N):
    if letter[i] == "T":
        t_cnt += 1
    else:
        a_cnt += 1
    last = letter[i]

if t_cnt == a_cnt:
    if last == "T":
        print("A")
    else:
        print("T")

else:
    if t_cnt > a_cnt:
        print("T")
    else:
        print("A")