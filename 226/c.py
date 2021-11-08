import sys
sys.setrecursionlimit(10 ** 7)
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())


N = II()
node = [[] for _ in range(N)]
seen = [True]*N
cost = [[] for _ in range(N)]

for i in range(N):
    time, *syugyo = MI()
    for j in syugyo[1:]:
        node[i].append(j-1)
    cost[i] = time
ans = cost[N-1]


def dfs(u):
    seen[N-1] = False
    global ans
    for v in node[u]:
        if seen[v]:
            seen[v] = False
            ans += cost[v]
            dfs(v)


dfs(N-1)
# print(seen)
# print(cost)
print(ans)
