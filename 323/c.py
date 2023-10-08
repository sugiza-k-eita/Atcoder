import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)


N, M = MI()
A = LI()

box = [input() for _ in range(N)]


scores = [sum(A[j] for j in range(M) if box[i][j] == 'o') + i for i in range(N)]

for i in range(N):
    max_other_score = max(scores[j] for j in range(N) if j != i)
    needed_score = max_other_score + 1 - scores[i]
    max_available_score = sum(A[j] for j in range(M) if box[i][j] == 'x')
    

    if needed_score <= max_available_score:
        remaining_problems = sorted([A[j] for j in range(M) if box[i][j] == 'x'], reverse=True)
        current_score = 0
        count = 0

        while current_score < needed_score:
            current_score += remaining_problems[count]
            count += 1
        print(count)

