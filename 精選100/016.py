from itertools import permutations, chain
N = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))
P_cnt = 0
Q_cnt = 0
cnt = 0
for per in permutations(range(1, N+1)):
    cnt += 1
    if per == P:
        P_cnt = cnt
    if per == Q:
        Q_cnt = cnt
print(abs(P_cnt-Q_cnt))
