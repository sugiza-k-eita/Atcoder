import bisect
N = int(input())
Ns = list(map(int, input().split()))
Q = int(input())
T = list(map(int, input().split()))
cnt = 0
for t in T:
    index = bisect.bisect_left(Ns, t)
    if index == N:
        continue
    if Ns[index] == t:
        cnt += 1
print(cnt)
