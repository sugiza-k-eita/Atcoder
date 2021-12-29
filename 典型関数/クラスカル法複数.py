"""
https://www.ioi-jp.org/camp/2010/2010-sp-tasks/2010-sp-day3_22.pdf
最小領域木を複数作る場合
"""

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

from typing import List

class UnionFind:
    """0-indexed"""

    def __init__(self, n):
        self.n = n
        self.parent = [-1] * n
        self.__group_count = n

    def unite(self, x, y) -> bool:
        """xとyをマージ"""
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        self.__group_count -= 1

        if self.parent[x] > self.parent[y]:
            x, y = y, x

        self.parent[x] += self.parent[y]
        self.parent[y] = x

        return True

    def is_same(self, x, y) -> bool:
        """xとyが同じ連結成分か判定"""
        return self.root(x) == self.root(y)

    def root(self, x) -> int:
        """xの根を取得"""
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

class Kruskal:

    class Edge:
        def __init__(self, start, end, cost):
            self.start, self.end, self.cost = start, end, cost

        def __lt__(self, another):
            return self.cost < another.cost

    def __init__(self, node_size,town_size):
        self._node = node_size
        self._town= town_size
        self._edge_list = []

    def add_edge(self, start, end, cost):
        self._edge_list.append(self.Edge(start, end, cost))
        #_edge_listというlistにstart,end,costを格納

    def solve(self):
        uf = UnionFind(self._node)
        #nodeの数をunionfindして、
        res = 0
        #最終的な残す辺の数
        town_count = 0
        #残す辺の数
        self._edge_list.sort()
        #costが小さい順に出力する
        for e in self._edge_list:
            if town_count == self._node - self._town:
                break
            #辺の数分、展開
            elif not uf.is_same(e.start, e.end):
                #uとvが同じグループに分類されていなかったら
                uf.unite(e.start, e.end)
                #くっつける
                res += e.cost
                town_count += 1
                #そして最小合計コストとして足す
        return res


V,E,K = MI()
kr = Kruskal(V,K)

box = []
town = 0
#開催都市の個数
for _ in range(E):
    start,end,cost =MI()
    start -= 1
    end -= 1
    box.append([cost,start,end])
box.sort()
for b in box:
    cost,start,end = b[0],b[1],b[2]
    kr.add_edge(start, end, cost)
    
ans= kr.solve()
print(ans)
