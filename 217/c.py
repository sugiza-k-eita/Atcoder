N = int(input())
ns = list(map(int, input().split()))
Q = [0]*N
for i in range(N):
    Q[ns[i]-1] = i + 1

print(*Q, sep=" ")
