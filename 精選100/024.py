import sys
sys.setrecursionlimit(10 ** 6)

N = int(input())
edges = [[] for i in range(N)]
seen = [True]*N
first = [0]*N
first[0] = 1
second = [0]*N
cnt = 1
for i in range(N):
    index, kazu, *ns = map(int, input().split())
    for j in ns:
        edges[i].append(j-1)


def dfs(u):
    global cnt
    cnt += 1
    if not edges[u]:
        second[u] = cnt

    for v in edges[u]:
        if seen[v]:
            seen[v] = False
            first[v] = cnt
            dfs(v)
            second[v] = cnt
            cnt += 1
    second[u] = cnt


for i in range(N):
    if seen[i]:
        seen[i] = False
        first[i] = cnt
        dfs(i)
        cnt += 1
# print(seen)
# print(first)
# print(second)

for i, f, s in zip(range(1, N+1), first, second):
    print(i, f, s)
