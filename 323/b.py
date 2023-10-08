import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = int(input())


p = []
for i in range(N):
    pi = S()
    p.append(pi)


score = [[0, i+1] for i in range(N)]

for i in range(N):
    pi = p[i]
    for j in range(N):
        if pi[j] == "o":
            score[i][0] += -1

score.sort()

ans = []

for i in range(N):
    ans.append(score[i][1])

print(*ans, sep=" ")



