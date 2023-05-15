N = int(input())
A = list(map(int, input().split()))

ans = []
for i in range(N-1):
    ans.append(A[i])
    if abs(A[i]-A[i+1]) == 1:
        continue
    elif A[i] < A[i+1]:
        add_list = []
        for  j in range(A[i]+1, A[i+1]):
            add_list.append(j)
        ans.extend(add_list)

    elif A[i] > A[i+1]:
        add_list = []
        for  j in range(A[i]-1, A[i+1], -1):
            add_list.append(j)
        ans.extend(add_list)
ans.append(A[-1])

print(*ans, sep=" ")
