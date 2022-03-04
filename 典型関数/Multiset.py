# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py
# https://atcoder.jp/contests/abc241/tasks/abc241_d

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

"""
multisetは、集合を扱うデータ構造です。setと異なり、同じ値の要素を複数持つことができます。
SortedSet の多重集合版です。同じ要素を複数入れることができます。SortedSet からの変更点は以下の通りです。

s.add(x)
x が s に含まれているかどうかに関わらず x を追加します。何も返しません。O(√N) amotized / O(N) worst

s.discard(x)
x が s に含まれていれば x を 1 個 削除し、True を返します。O(√N) amotized / O(N) worst
(C++ の std::multiset::erase には x を全て削除してしまうという罠があります。)

s.count(x)
s に含まれる x の個数を返します。O(√N) (定数倍が小さい)
"""

"""
主に使うのは、count,add,discard,であとは最大値、最小値関係
"""
class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        #s に含まれる x の個数を返します
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        #x が s に含まれているかどうかに関わらず x を追加します。何も返しません
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        #x が s に含まれていれば x を 1 個 削除し、True を返します
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        #x より小さいかつ最大の要素を返します。存在しなければ None をを返します
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        #x以下かつ最大の要素を返す。そんざいしなければNoneを返す
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        #x+1以上で最小のものを返す
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        #以上で最小のものを返す
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        #x より小さい要素の数を返します。
        # x が s に含まれている場合は list(s).index(x) に相当
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        #x 以下の要素の数を返します
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

st=SortedMultiset()
# for i in range(Q):
#   A=LI()
#   if A[0]==1:
#     st.add(A[1])
#   else:
#     a,x,k=A
#     if a==2:
#       d=st.index_right(x)
#       if d-k>=0:
#         print(st[d-k])
#       else:
#         print(-1)
#     else:
#       d=st.index(x)
#       if d+k-1<len(st):
#         print(st[d+k-1])
#       else:
#         print(-1)
      