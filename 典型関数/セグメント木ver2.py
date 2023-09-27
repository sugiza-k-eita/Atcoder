def segfunc(x,y):
    #和ならば
    return x+y
    # #最小値なら
    # return min(x,y)

class SegTree:
    def __init__(self,init_val,segfunc,ide_ele):
        n = len(init_val)#葉の要素を格納
        self.segfunc = segfunc#求められるquery
        self.ide_ele = ide_ele#初期値
        self.num = 1<<(n-1).bit_length()#葉の要素の数を2の指数関数上に揃える
        self.tree = [ide_ele]*2*self.num#親の要素含めて葉の要素の2倍必要
        
        for i in range(n):
            self.tree[self.num+i] = init_val[i]#葉に初期値を代入
        #numは葉の一番左側の要素
        for i in range(self.num-1,0,-1):
            self.tree[i] = self.segfunc(self.tree[2*i],self.tree[2*i+1])#親の要素iは2つの子の要素[2i,2i+1]で決まる
    
    def add(self,k,x):
        k += self.num
        self.tree[k] += x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    def update(self,k,x):
        k += self.num
        self.tree[k] = x
        while k>1:
            self.tree[k>>1] = self.segfunc(self.tree[k],self.tree[k^1])
            k >>= 1
    
    def query(self,l,r):
        res = self.ide_ele
        l += self.num
        r += self.num
        while l<r:
            if l&1:
                res = self.segfunc(res,self.tree[l])
                l += 1
            if r&1:
                res = self.segfunc(res,self.tree[r-1])
            l >>= 1
            r >>= 1
        return res

N,Q = map(int, input().split())
ini = 2**31-1
import math
st = SegTree([ini]*(N+1),segfunc,0)
"""
最小値の場合第三引数はmath.inf
"""
for i in range(Q):
    cmd,x,y = map(int, input().split())
    if cmd == 0:
        st.add(x,y)
    else:
        ans = st.query(x,y+1)
        print(ans)

