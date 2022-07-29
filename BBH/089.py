from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


N, X,Y = MI()

node = [[] for i in range(N)]

for i in range(1,N-1):
    node[i].append(i-1)
    node[i].append(i+1)

node[0].append(1)
node[N-1].append(N-2)
node[X-1].append(Y-1)
node[Y-1].append(X-1)

# for x in node:
#     print(x)


def bfs(Node,start,N):
    seen = [False]*N
    seen[start] = True
    dist = [0]*N
    que = deque()
    que.append(start)

    while que:
        now = que.popleft()
        for next in Node[now]:
            if seen[next] == True:
                continue
            elif seen[next] == False:
                seen[next] = True
                dist[next] += dist[now]+1
                que.append(next)
    return dist

cnt = [0]*(N)
for i in range(N):
    a = bfs(node,i,N)
    for j in a:
        cnt[j] += 1

for i in range(1,N):
    print(cnt[i]//2)