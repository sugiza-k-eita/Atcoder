import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import bisect

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


N = II()
node_cnt = []
node = []
for i in range(N):
    A,B = MI()
    node_cnt.append(A)
    node_cnt.append(B)
    node.append([A,B])

if 1 not in node_cnt:#そもそも1階とどこかの階にはしごがかかっていなかったら1階から動けないので
    print(1)
    exit()

neo_box = list(set(node_cnt))#出てくる階の数を数えている
neo_box.sort()#bisectを使うので、ソートしておく
uf = UnionFind(len(neo_box))#その階の数だけunionfindのnodeを設ける

for i in range(N):
    A = node[i][0]
    B = node[i][1]
    A_ind = bisect.bisect_left(neo_box,A)#A階は、(ソートされた)出てくる階の中だと何番目のindexを持つのか
    B_ind = bisect.bisect_left(neo_box,B)#A階は、(ソートされた)出てくる階の中だと何番目のindexを持つのか
    uf.unite(A_ind,B_ind)#AのindとBのindをつなげる

for i in range(len(neo_box)-1,0,-1):#後ろから、つまり大きい数字から探索
    if uf.is_same(0,i):#もし、index_0とindex_iが連結されているのなら、
        print(neo_box[i])#そのindexを持つ階には到達可能である
        exit()
#どの階にも到達できなかった場合
print(1)
exit()