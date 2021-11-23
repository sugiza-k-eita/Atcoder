import sys
sys.setrecursionlimit(10**7)

N = int(input())
seen = [0] * N
edge = [[] for i in range(N)]

for i in range(N-1):
    a, b = map(int, input().split())
    edge[a-1].append(b-1)
    edge[b-1].append(a-1)


def dfs(u):
    cnt = 0
    for v in edge[u]:
        if seen[v] == 0:
            seen[v] = seen[u]+1
            dfs(v)


ans = 0
seen[0] = 1
dfs(0)
highest = seen.index(max(seen))
# print(highest)
# print(seen)
seen = [0]*N
seen[highest] = 1
dfs(highest)
ans = max(seen)
print(ans)
