import sys
sys.setrecursionlimit(10**7)
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


N, X = MI()
X -= 1
freinde = LI()
edge = [[] for i in range(N)]
seen = [False]*N


for i in range(N):
    edge[i].append(freinde[i]-1)
cnt = 1

seen[X] = True


def dfs(u):
    global cnt
    for v in edge[u]:
        if seen[v] == False:
            seen[v] = True
            cnt += 1
            dfs(v)
        else:
            break


dfs(X)
print(cnt)
# print(seen)
