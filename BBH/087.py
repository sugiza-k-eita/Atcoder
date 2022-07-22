import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,M,K = MI()

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

friend_r = [[] for _ in range(N)]
#既存の友達関係を管理
uf = UnionFind(N)
for m in range(M):
    A,B = MI()
    A -= 1
    B -= 1
    #ufに合わせるため、indexは0始まりにする
    friend_r[A].append(B)
    friend_r[B].append(A)
    #友達関係を追加
    uf.unite(A,B)
    # AとBは同じ連結成分に属する

ans = [0]*N
#N人について、友達候補の人数を管理する

for i in range(N):
    ans[i] = uf.size(i) - 1 - len(friend_r[i])
    #友達候補 = 同じ連結成分に属する人 - 自分自身 - 既存の友達

for k in range(K):
    C,D = MI()
    C -= 1
    D -= 1
    if uf.is_same(C,D):
        #CとDが同じ連結成分ならば、友達候補は-1
        #なぜならブロック関係であるから
        ans[C] -= 1
        ans[D] -= 1

print(*ans, sep= " ")
