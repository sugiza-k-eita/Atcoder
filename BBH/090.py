import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
edges = [[] for i in range(N)]
seen = [True]*N
#dfsの時、一度来たnodeには、行く必要がないからそのflg
ans = [1]*N
#答えをすべて黒だと仮定する

for i in range(N-1):
    u,v,w = MI()
    u,v = u-1,v-1
    #indexを0始まりにするために-1をする
    edges[u].append([v,w])
    edges[v].append([u,w])

def dfs(u):
    for v,w in edges[u]:
        if seen[v] == False:
            #一度訪れたことがあるのではあれば、そのnodeに対しては操作を行わない
            continue
        else:#一度も訪れたことがなければ
            seen[v] = False
            #二度と訪れないようにflgを更新
            if w %2 == 0:
                #もし距離が偶数なら
                ans[v] = ans[u]
                #同じ色に着色
            else:
                #もし距離が奇数なら
                ans[v] = ans[u]* -1
                #違う色に着色 (操作をしやすくするために0にする代わりに-1倍)
            dfs(v)

seen[0] = False
#seen[0]はスタート位置だから訪問済み
dfs(0)

for i in ans:
    if i == -1:
        #-1なら1(黒)と異なる色だから
        print(0)
    else:
        print(i)