#https://qiita.com/R_olldIce/items/f2f7930e7f67963f0493
#https://www.slideshare.net/hcpc_hokudai/binary-indexed-tree
#先頭からある数までの累積和が知りたいときにlogNで行う処理
#途中で値の更新があるときに使う
#https://atcoder.jp/contests/practice2/tasks/practice2_b


class Fenwick_Tree:
    def __init__(self, n):
        self._n = n
        self.data = [0] * n

    def add(self, p, x):
        assert 0 <= p < self._n
        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        #([l,r)の部分和)=(r−1までの部分和)−(l−1までの部分和)
        assert 0 <= l <= r <= self._n
        return self._sum(r) - self._sum(l)

    def _sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s


#https://qiita.com/u2dayo/items/5e2034dbc65ea56ab6a7#d%E5%95%8F%E9%A1%8Credoctaswapii1
class FenwickTree:
    def __init__(self, n):
        self.__array = [0] * n
        self.__size = n + 1
        self.__container = [0] * (n + 1)
        self.__depth = n.bit_length()

    def add(self, i, x):
        """a[i]にxを加算"""
        self.__array[i] += x
        i += 1
        while i < self.__size:
            self.__container[i] += x
            i += i & (-i)

    def sum(self, r):
        """[0, r) の総和"""
        s = 0
        while r > 0:
            s += self.__container[r]
            r -= r & (-r)
        return s