from itertools import product, repeat
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = float('inf')
for bit in product((True, False), repeat=N):
    Ns = []
    if sum(bit) != K:
        continue
    elif bit[0] == False:
        continue
    box = []
    cost = 0
    for i in range(N):
        if bit[i]:
            box.append(i)
    for i in box:
        Ns.append(A[i])
    border = [0]
    for j in range(1, len(box)):
        if border >= Ns[j]:
            cost += border-Ns[j]+1
            border += 1
        else:
            border = Ns[j]
    ans = min(ans, cost)
print(ans)
