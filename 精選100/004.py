from itertools import combinations
N, M = map(int, input().split())
scores = []
for i in range(N):
    A = list(map(int, input().split()))
    scores.append(A)


total = 0
for i in combinations(range(M), 2):
    score = 0
    for j in range(N):
        score += max(scores[j][i[0]], scores[j][i[1]])
    total = max(total, score)

print(total)
