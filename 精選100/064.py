import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

V,E = MI()

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

class Kruskal:

    class Edge:
        def __init__(self, start, end, cost):
            self.start, self.end, self.cost = start, end, cost

        def __lt__(self, another):
            return self.cost < another.cost

    def __init__(self, node_size):
        self._node = node_size
        self._edge_list = []

    def add_edge(self, start, end, cost):
        self._edge_list.append(self.Edge(start, end, cost))
        #_edge_listというlistにstart,end,costを格納

    def solve(self):
        uf = UnionFind(self._node)
        #nodeの数をunionfindして、
        res = 0
        #最終的な残す辺の数
        edge_count = 0
        #残す辺の数
        self._edge_list.sort()
        #costが小さい順に出力する
        for e in self._edge_list:
            #辺の数分、展開
            if not uf.same(e.start, e.end):
                #uとvが同じグループに分類されていなかったら
                uf.unite(e.start, e.end)
                #くっつける
                res += e.cost
                #そして最小合計コストとして足す
                edge_count += 1
                if edge_count == self._node-1:
                    #残す辺の数がnodeの数－１になったらbreak
                    break
        return res,self._edge_list

kr = Kruskal(V)
for _ in range(E):
    s, t, w = map(int, sys.stdin.readline().split())
    kr.add_edge(s, t, w)
ans,box = kr.solve()
print(ans)
