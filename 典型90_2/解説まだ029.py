import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
def op(x, y):
    return min(x,y)

def e():
    return 2147483647
class SegTree:#一点更新,区間取得
    def __init__(self, op, e, n, v=None):
        self._n = n
        self._op = op
        self._e = e
        self._log = (n - 1).bit_length()
        self._size = 1 << self._log
        self._d = [self._e()] * (self._size << 1)
        if v is not None:
            for i in range(self._n):
                self._d[self._size + i] = v[i]
            for i in range(self._size - 1, 0, -1):
                self._d[i] = self._op(self._d[i << 1], self._d[i << 1 | 1])

    def set(self, p, x):
        p += self._size
        self._d[p] = x
        while p:
            self._d[p >> 1] = self._op(self._d[p], self._d[p ^ 1])
            p >>= 1

    def get(self, p):
        return self._d[p + self._size]

    def prod(self, l, r):
        sml, smr = self._e(), self._e()
        l += self._size
        r += self._size
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    def all_prod(self):
        return self._d[1]
N,Q = MI()
if N == 1:
    N+=1

st = SegTree(op,e,N)
for q in range(Q):
    com,x,y = MI()
    if com == 0:
        st.set(x,y)
        # print(st._d)
    else:
        val = st.prod(x,y+1)
        print(val)
