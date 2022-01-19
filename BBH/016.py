from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,X,Y = MI()
node = [[] for i in range(N)]
for i in range(N-1):
    node[i].append(i+1)
    node[i+1].append(i)

node[X-1].append(Y-1)
node[Y-1].append(X-1)

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
    ans = bfs(node,i,N)
    for j in ans:
        cnt[j] += 1

for i in cnt[1:]:
    print(i//2)
    

    