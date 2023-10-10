N = int(input())

letter = input()

left = 0
ans = [0 for i in range(N)]
for right in range(1,N):
    if letter[left] == letter[right]:
        continue

    for j in range(left,right):
        ans[j] = N-right
    left = right
# print(ans)
print(sum(ans[:-1]))