from itertools import product, repeat
N, M = map(int, input().split())
switches = []
K = []

for i in range(M):
    ns = list(map(int, input().split()))
    k = ns.pop(0)
    K.append(k)
    switches.append(ns)
P = list(map(int, input().split()))
cnt = 0
flg = 0
for i in product((0, 1), repeat=N):
    flg = 0
    for j in range(M):
        tmp = 0
        for k in switches[j]:
            tmp += i[k-1]
        if tmp % 2 != P[j]:
            continue
        flg += 1
    if flg == M:
        cnt += 1
print(cnt)
