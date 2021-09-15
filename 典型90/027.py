N = int(input())
box = {}
ans = []
for i in range(N):
    a = input()
    if not a in box:
        box[a] = 1
        ans.append(i+1)
for i in ans:
    print(i)
