N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
cnt = 0
for i in range(N):
    cnt += abs(A[i]-B[i])
if cnt > K:
    print("No")
else:
    if (K-cnt) % 2 == 0:  # Kkが奇数ならcnt(AとBの差分も奇数)
        print("Yes")
    else:
        print("No")
