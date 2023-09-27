"""
一点更新、区間最小
https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_A
https://onlinejudge.u-aizu.ac.jp/solutions/problem/DSL_2_A
"""
import sys

# READ_FROM_FILE = True
READ_FROM_FILE = False


class RangeMinMaxQuery:
    def __init__(self, n, init_val, is_min=True):
        self._n = 1
        self._is_min = is_min
        while self._n < n:
            self._n <<= 1
        self._data = [init_val] * (2 * self._n - 1)
        return

    def _query_sub(self, s, t, k, left, right):
        if right <= s or t <= left:
            if self._is_min:
                return float('inf')
            else:
                return -float('inf')
        if s <= left and right <= t:
            return self._data[k]
        else:
            mid = (left + right) // 2
            k2 = 2 * k
            l_val = self._query_sub(s, t, k2 + 1, left, mid)
            r_val = self._query_sub(s, t, k2 + 2, mid, right)
            if self._is_min:
                return min(l_val, r_val)
            else:
                return max(l_val, r_val)

    # i: zero-based
    def update(self, i, x):
        i += self._n - 1
        self._data[i] = x
        while i > 0:
            i = (i - 1) // 2
            i2 = 2 * i
            left = i2 + 1
            right = i2 + 2
            if self._is_min:
                self._data[i] = min(self._data[left], self._data[right])
            else:
                self._data[i] = max(self._data[left], self._data[right])
        return

    # [s, t), zero-based
    def find(self, s, t):
        return self._query_sub(s, t, 0, 0, self._n)


def main():
    if READ_FROM_FILE:
        f = open('test0.txt', 'r')
    else:
        f = sys.stdin

    n, q = map(int, f.readline().split())
    init_val = 2147483647
    rmq = RangeMinMaxQuery(n, init_val, True)

    for _ in range(q):
        query_tuple = tuple(map(int, f.readline().split()))
        if query_tuple[0] == 0:
            i = query_tuple[1]
            x = query_tuple[2]
            rmq.update(i, x)
        else:
            s = query_tuple[1]
            t = query_tuple[2] + 1
            min_val = rmq.find(s, t)
            print(min_val)

    if READ_FROM_FILE:
        f.close()
    return


if __name__ == '__main__':
    main()



"""
一点加算、区間和
https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_B
"""
import sys

# READ_FROM_FILE = True
READ_FROM_FILE = False


class RangeSumQuery:
    def __init__(self, n):
        self._n = n
        self._bit = [0] * (self._n + 1)
        return

    def _query_sub(self, i):
        s = 0
        while i > 0:
            s += self._bit[i]
            i -= i & -i
        return s

    # i: one-based
    def add(self, i, x):
        while i <= self._n:
            self._bit[i] += x
            i += i & -i
        return

    # [s, t]: one-based
    def get_sum(self, s, t):
        return self._query_sub(t) - self._query_sub(s - 1)


def main():
    if READ_FROM_FILE:
        f = open('test0.txt', 'r')
    else:
        f = sys.stdin

    n, q = map(int, f.readline().split())
    rsq = RangeSumQuery(n)

    for _ in range(q):
        query_tuple = tuple(map(int, f.readline().split()))
        if query_tuple[0] == 0:
            i = query_tuple[1]
            x = query_tuple[2]
            rsq.add(i, x)
        else:
            s = query_tuple[1]
            t = query_tuple[2]
            result = rsq.get_sum(s, t)
            print(result)

    if READ_FROM_FILE:
        f.close()
    return


if __name__ == '__main__':
    main()


"""
区間更新、一点出力
https://onlinejudge.u-aizu.ac.jp/problems/DSL_2_D
"""
import sys

# READ_FROM_FILE = True
READ_FROM_FILE = False


class RangeUpdateQuery:
    def __init__(self, n, init_val):
        self._n = 1
        while self._n < n:
            self._n <<= 1
        self._lazy = [-1] * (2 * self._n - 1)
        for i in range(self._n):
            self._lazy[i + self._n - 1] = init_val
        return

    def _eval(self, k):
        if self._lazy[k] < 0:
            return
        if k < self._n - 1:
            k2 = 2 * k
            self._lazy[k2 + 1] = self._lazy[k]
            self._lazy[k2 + 2] = self._lazy[k]
            self._lazy[k] = -1
        return

    def _update_sub(self, s, t, x, k, left, right):
        if self._lazy[k] >= 0:
            self._eval(k)

        if right <= s or t <= left:
            return
        if s <= left and right <= t:
            self._lazy[k] = x
            return

        mid = (left + right) // 2
        k2 = 2 * k
        self._update_sub(s, t, x, k2 + 1, left, mid)
        self._update_sub(s, t, x, k2 + 2, mid, right)
        return

    # i: zero-based
    def find(self, i):
        i += self._n - 1

        result = self._lazy[i]
        i = (i - 1) // 2
        while i >= 0:
            if self._lazy[i] >= 0:
                result = self._lazy[i]
            i = (i - 1) // 2
        return result

    # [s, t), zero-based
    def update(self, s, t, x):
        self._update_sub(s, t, x, 0, 0, self._n)
        return


def main():
    if READ_FROM_FILE:
        f = open('test0.txt', 'r')
    else:
        f = sys.stdin

    n, q = map(int, f.readline().split())
    init_val = 2147483647
    ruq = RangeUpdateQuery(n, init_val)

    for _ in range(q):
        query_tuple = tuple(map(int, f.readline().split()))
        if query_tuple[0] == 0:
            s = query_tuple[1]
            t = query_tuple[2] + 1
            x = query_tuple[3]
            ruq.update(s, t, x)
        else:
            i = query_tuple[1]
            val = ruq.find(i)
            print(val)

    if READ_FROM_FILE:
        f.close()
    return


if __name__ == '__main__':
    main()



"""
区間加算、一点出力
"""
import sys

# READ_FROM_FILE = True
READ_FROM_FILE = False


class RangeAddQuery:
    def __init__(self, n):
        self._n = 1
        while self._n < n:
            self._n <<= 1
        self._lazy = [0] * (2 * self._n - 1)
        return

    def _add_sub(self, s, t, x, k, left, right):
        if right <= s or t <= left:
            return
        if s <= left and right <= t:
            self._lazy[k] += x
            return

        mid = (left + right) // 2
        k2 = 2 * k
        self._add_sub(s, t, x, k2 + 1, left, mid)
        self._add_sub(s, t, x, k2 + 2, mid, right)
        return

    # i: zero-based
    def get(self, i):
        i += self._n - 1

        result = self._lazy[i]
        i = (i - 1) // 2
        while i >= 0:
            result += self._lazy[i]
            i = (i - 1) // 2
        return result

    # [s, t), zero-based
    def add(self, s, t, x):
        self._add_sub(s, t, x, 0, 0, self._n)
        return


def main():
    if READ_FROM_FILE:
        f = open('test0.txt', 'r')
    else:
        f = sys.stdin

    n, q = map(int, f.readline().split())
    raq = RangeAddQuery(n)

    for _ in range(q):
        query_tuple = tuple(map(int, f.readline().split()))
        if query_tuple[0] == 0:
            s = query_tuple[1] - 1
            t = query_tuple[2]
            x = query_tuple[3]
            raq.add(s, t, x)
        else:
            i = query_tuple[1] - 1
            val = raq.get(i)
            print(val)

    if READ_FROM_FILE:
        f.close()
    return


if __name__ == '__main__':
    main()

