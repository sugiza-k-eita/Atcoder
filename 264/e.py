import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

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

N,M,E = MI()
node = [[] for i in range(E)]
for i in range(E):
    u,v = MI()
    u -= 1
    v -= 1
    if u >  N-1:
        u = N#uが発電所の場合、発電所はN番目にする
    if v > N-1:
        v = N#vが発電所の場合、発電所はN番目にする
    node[i] = [u,v]


uf = UnionFind(N+1)
#N+1番目は発電所

Q = II()
flg = [True] * E#最終的につながっているかどうか
push = []#最終的につながっているかどうか
for q in range(Q):
    x = II()
    x -= 1
    flg[x] = False
    push.append(x)

push.reverse()
# print(push)
# print(flg)

for i in range(E):
    if flg[i]:
        # print(node[i])
        uf.unite(node[i][0],node[i][1])


# print(uf.all_sizes())

cnt  = []
for i in range(Q):
    cnt.append(uf.size(N)-1)
    x = push[i]
    uf.unite(node[x][0],node[x][1])

for i in cnt[::-1]:
    print(i)