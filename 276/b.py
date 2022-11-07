import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,M = MI()
node = [[] for i in range(N)]
for i in range(M):
    a,b = MI()
    a -= 1
    b -= 1
    node[a].append(b+1)
    node[b].append(a+1)

for i in range(N):
    node[i].sort()
    print(len(node[i]),*node[i], sep=" ")

