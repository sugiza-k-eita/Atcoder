from itertools import product, repeat
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
M = list(map(int, input().split()))
ans = []
for i in product((0, 1), repeat=N):
    tmp = 0
    for j in range(len(i)):
        if i[j] == 0:
            continue
        else:
            tmp += A[j]
    ans.append(tmp)

for i in M:
    if i in ans:
        print("yes")
    else:
        print("no")
