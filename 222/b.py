N, P = map(int, input().split())
ns = list(map(int, input().split()))
cnt = 0
for i in range(N):
    if ns[i] < P:
        cnt += 1
print(cnt)
