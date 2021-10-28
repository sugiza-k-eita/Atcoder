# 絶対値の最小化は中央値を使う
import statistics
N = int(input())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
AA = sorted(A)
BB = sorted(B)
Entrance = statistics.median(AA)
Exit = statistics.median(BB)
print(Exit)
ans = 10**18
for entrance in A:
    for exit in B:
        tmp = 0
        for i in range(N):
            tmp += B[i]-A[i]
            tmp += abs(entrance-A[i])
            tmp += abs(exit-B[i])
        ans = min(ans, tmp)
print(ans)
