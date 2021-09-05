S, T = input().split()

box = []
box.append(S)
box.append(T)
box.sort()
if S == box[0]:
    print("Yes")
else:
    print("No")
