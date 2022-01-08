import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M,Q =MI()
box = [[0]*(N+1) for i in range(N+1)]
for i in range(M):
    L,R = MI()
    box[L][R] += 1

for h in range(1,N+1):
    for w in range(1,N+1):
        box[h][w] += box[h][w-1]

for w in range(1,N+1):
    for h in range(1,N+1):
        box[h][w] += box[h-1][w]

# for xx in box:
#     print(xx)

for j in range(Q):
    p,q = MI()
    p -=1
    ans = box[p][p] + box[q][q] - box[p][q] -box[q][p]
    print(ans)