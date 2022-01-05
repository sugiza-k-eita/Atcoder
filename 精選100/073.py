"""
0,0 から X,Y までの移動回数は(X+Y)/3回
なぜなら、一度に移動するマスは(1,2) or (2,1)なので
また、
(1,2)→(0,1)+(1,1)
(2,1)→(1,0)+(1,1)と考えると
どちらの操作をしても、必ず(1,1)は移動する
よって、(X+Y)/3回は(1,1)に移動する
そして、(X+Y)/3回のうち、何回かは(0,1)移動し、それ以外は(1,0)に移動する
"""

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
mod=10**9 + 7
def comb(n, r, mod=10**9 + 7):
    """
    nCr を modを法として求める
    計算量はO(r)
    modがNoneの場合は modを取らない結果を返す
    mod はNoneか素数であることを仮定する
    """
    p = 1
    for i in range(r):
        p *= (n - i) * pow(i + 1, mod-2, mod)
        p = p % mod
 
    return p

X,Y = MI()
if (X+Y)%3 != 0:
    print(0)
elif X+Y == 3:
    print(1)
else:
    n=(X+Y)//3#移動回数
    new_x = X-n
    new_y = Y-n
    #new_xは上だけに動いた回数 new_yは右だけに動いた回数
    ans = comb(new_x+new_y,new_x)
    print(ans%mod)



