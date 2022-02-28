N = int(input())
A = list(map(int, input().split()))
stack = []

cnt = 0

for a in A:
    if len(stack) != 0 and stack[-1][0] == a:
        stack[-1][1] += 1
    else:
        stack.append([a, 1])
    cnt += 1
    if stack[-1][0] == stack[-1][1]:
        cnt -= stack[-1][0]
        stack.pop()

    print(cnt)


