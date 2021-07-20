letter = str(input())
split_ns = []
for i in range(len(letter)):
    split_ns.append(letter[i])
if split_ns[0] == split_ns[1] and split_ns[0] == split_ns[2]:
    print("Won")
else:
    print("Lost")
