N,Q = map(int, input().split())


node = [set() for i in range(N)]
cnt = N
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        u = query[1]-1
        v = query[2]-1
        origin_u = len(node[u])
        origin_v = len(node[v])
        node[u].add(v)
        node[v].add(u)
        if origin_u == 0:
            cnt -= 1
        if origin_v == 0:
            cnt -= 1
        print(cnt)

    elif query[0] == 2:
        u = query[1]-1
        if len(node[u]) == 0:
            print(cnt)
    
        else:
            for v in node[u]:
                node[v].discard(u)
                if len(node[v]) == 0:
                    cnt += 1
            node[u] = set()
            cnt += 1
            print(cnt)
