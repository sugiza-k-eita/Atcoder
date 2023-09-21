from itertools import combinations
from bisect import bisect_right

N, K, P = map(int, input().split())
A = list(map(int, input().split()))
if N == 1:
    if A[0] <= P:
        print(1)
    else:
        print(0)
    exit()

if K == N:
    if sum(A)<= P:
        print(1)
    else:
        print(0)
    exit()


head_half = N // 2
tail_half = N -head_half
first_half = A[:head_half]
second_half = A[head_half:]

first_half_comb = [[] for _ in range(head_half+1)]
second_half_comb = [[] for _ in range(tail_half+1)]

for i in range(head_half+1):
    for comb in combinations(first_half, i):
        first_half_comb[i].append(sum(comb))

for i in range(tail_half+1):
    for comb in combinations(second_half, i):
        second_half_comb[i].append(sum(comb))

for i in range(head_half+1):
    first_half_comb[i].sort()
for i in range(tail_half+1):
    second_half_comb[i].sort()


ans = 0
for i in range(max(0, K-tail_half), min(K+1, head_half+1)):
    for p1 in first_half_comb[i]:
        ind = bisect_right(second_half_comb[K-i], P - p1)      # P-p1 以下の要素数
        ans += ind

print(ans)
