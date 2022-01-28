"""
重み付き無向グラフの最小全域木を求めるためのアルゴリズム
Kruskal法では、重みの小さい順に辺を見ていき、閉路や多重辺がなければTに辺を追加するという方法をとります
計算量はO(|E|log|V|)となります
"""

import sys

def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M,Q = MI()

class UnionFind:
    def __init__(self, node_size):
        self._node = node_size
        self.par = [i for i in range(self._node)]
        self.rank = [0] * self._node

    def find(self, ver):
        if self.par[ver] == ver:
            return ver
        else:
            self.par[ver] = self.find(self.par[ver])
            return self.par[ver]

    def unite(self, ver1, ver2):
        ver1, ver2 = self.find(ver1), self.find(ver2)
        if ver1 == ver2:
            return
        if self.rank[ver1] < self.rank[ver2]:
            ver1, ver2 = ver2, ver1
        self.par[ver2] = ver1
        if self.rank[ver1] == self.rank[ver2]:
            self.rank[ver1] += 1

    def same(self, ver1, ver2):
        return self.find(ver1) == self.find(ver2)


uf = UnionFind(N)
node = []
for _ in range(M):
    a, b, c = MI()
    a -= 1
    b -= 1
    node.append((c,a,b,-1))

for _ in range(Q):
    u,v,w = MI()
    u -= 1
    v -= 1
    node.append((w,u,v,_))

node.sort()
ans = [False]*Q
for c,a,b,flg in node:
    if flg == -1:
        uf.unite(a,b)
    if flg != -1:
        if uf.same(a,b):
            #同じ時は追加する必要なし
            ans[flg] = False
        else:
            ans[flg] = True

for xx in ans:
    if xx:
        print("Yes")
    else:
        print("No")
