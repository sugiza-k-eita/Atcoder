from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,Q = MI()
node = [[] for i in range(N)]
for i in range(N-1):
    a,b = MI()
    a -= 1
    b -= 1
    node[a].append(b)
cnt = [0 for i in range(N)]
for j in range(Q):
    p,x = MI()
    p -= 1
    cnt[p] += x

def bfs(Node,start,N):
    seen = [False]*N
    seen[start] = True
    dist = [0]*N
    dist[0] = cnt[0]
    que = deque()
    que.append(start)

    while que:
        now = que.popleft()
        for next in Node[now]:
            if seen[next] == True:
                continue
            elif seen[next] == False:
                seen[next] = True
                dist[next] += dist[now]+cnt[next]
                que.append(next)
    return dist

ans = bfs(node,0,N)
print(*ans, sep=" ")