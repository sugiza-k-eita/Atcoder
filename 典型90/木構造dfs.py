# https://atcoder.jp/contests/typical90/tasks/typical90_am

N = int(input())
G = [dict() for i in range(N)]
edges = []
for i in range(N-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a][b] = 1
    G[b][a] = 1
    edges.append((a, b))


def dfs_tree(G, root=0):
    N = len(G)
    stack = [root]
    parent = [-1] * N
    depth = [-1] * N
    depth[root] = 0
    euler = []
    while stack:  # dfs
        u = stack.pop()
        euler.append(u)
        if u >= 0:
            stack.append(~u)
            for v in G[u]:
                if depth[v] != -1:
                    continue
                depth[v] = depth[u] + 1
                parent[v] = u
                stack.append(v)
        else:
            u = ~u
    return depth, parent, euler


def subtree_size(depth, parent):  # O(N) 頂点iを根とする部分木のサイズのlist
    D = max(depth)
    children = [0]*N
    # layer[d] := depth[i]==dなる頂点iの集合
    layer = [[] for i in range(D+1)]
    for i in range(N):
        layer[depth[i]].append(i)
    # 葉から根へ伝搬させる
    for d in range(D, 0, -1):
        for i in layer[d]:
            children[parent[i]] += children[i]+1
    return children  # List[int]
