import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


N = II()

graph = [[] for i in range(N)]
node = 0
for i in range(N-1):
    a,b = MI()
    a -= 1
    b -= 1
    graph[a].append([b,i])#何番目の辺の情報かも付与 なぜなら今回は辺の色分けを行うため
    graph[b].append([a,i])
    node = max(node,a,b)

cnt = 0
for x in graph:
    cnt = max(cnt,len(x))#必要な色の数は、1頂点がもつ最大の辺の数と同じ

print(cnt)

ans = [0]*(N-1)
node = [[] for i in range(node)]

def dfs(u,p,c):# U = 現在地, p = 元いた場所,c = 元いた場所から現在地までの辺の色
    k =1
    for v,id in graph[u]:
        if v == p:#もといた場所に戻るのはだめ
            continue
        if k == c:#元いた場所から現在地までの色は使えないから+1
            k += 1
        
        ans[id] = k #id番目の辺の色はkとなる
        dfs(v,u,k)
        k += 1

dfs(0,-1,-1)#はじめは、元いた場所も、元いた場所からの辺もないから-1
for i in ans:
    print(i)