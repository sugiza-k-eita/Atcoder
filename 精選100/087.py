import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

"""
つなぐのは簡単だけど、切り離すのは難しい
切り離す処理→つなぐ処理を逆からやる
"""

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

    def size(self, x) -> int:
        """xが属する連結成分のサイズを取得"""
        return -self.parent[self.root(x)]

    def all_sizes(self) -> List[int]:
        """全連結成分のサイズのリストを取得 O(N)
        """
        sizes = []
        for i in range(self.n):
            size = self.parent[i]
            if size < 0:
                sizes.append(-size)
        return sizes

    def groups(self) -> List[List[int]]:
        """全連結成分の内容のリストを取得 O(N・α(N))"""
        groups = dict()
        for i in range(self.n):
            p = self.root(i)
            if not groups.get(p):
                groups[p] = []
            groups[p].append(i)
        return list(groups.values())

    @property
    def group_count(self) -> int:
        """連結成分の数を取得 O(1)"""
        return self.__group_count

N,M = MI()
edges = [[] for i in range(M)]
for i in range(M):
    a,b = MI()
    a -= 1
    b -= 1
    edges[i].append(a)
    edges[i].append(b)

edges.reverse()
all_broken = N*(N-1)//2
ans_box = [all_broken for i in range(M)]
uf = UnionFind(N)

for i in range(M):
    a,b = edges[i][0],edges[i][1]
    size_a = uf.size(a)
    size_b = uf.size(b)
    flg = uf.unite(a,b)
    if flg == True:
        #もともと別のグループであったら
        unite_size = size_a*size_b
        #くっつけることで、不便さは解消される
    else:
        #もともと同じグループであったら、不便さは解消されているので、
        #くっつけても不便さは解消されない
        unite_size = 0
    ans_box[i] = ans_box[i-1] - unite_size
ans_box.reverse()
ans_box.append(all_broken)

for i in range(1,M+1):
    print(ans_box[i])

