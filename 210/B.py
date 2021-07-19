n = int(input())
ns = str(input())

split_ns = []
for i in range(n):
    split_ns.append(int(ns[i]))

count = 0
for i in range(n):
    if split_ns[i] == 1:
        break
    else:
        count += 1
if count % 2 == 0:
    print("Takahashi")
else:
    print("Aoki")
