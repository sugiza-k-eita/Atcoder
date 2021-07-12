from itertools import product, repeat
n, m = map(int, input().split())
conditions = []
for i in range(m):
    a, b = map(int, input().split())
    conditions.append((a, b))

people = []
K = int(input())
for i in range(K):
    c, d = map(int, input().split())
    people.append((c, d))
print(conditions)
print(people)
ans = 0
# ↓これで0 or 1　のフラグを立てる処理を2**k回行っている
for bit in product((0, 1), repeat=K):
    count = [0]*(n+1)
    print(bit)
    # 皿の数、1のときは条件が満たされている
    for i in range(K):
        ball = people[i][bit[i]]
        count[ball] += 1
    score = 0
    for i in range(m):
        c, d = conditions[i]
        if count[c] > 0 and count[d] > 0:
            score += 1
    ans = max(ans, score)
print(ans)
