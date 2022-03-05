import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
"""
不可逆的だからdpでときたいけど、計算量がオーバーする
X+Y が3の倍数じゃないなら無理
X+Yが3の倍数のとき
何回(+1,+2)or (+2,+1)したか計算
"""
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
if (X + Y) % 3 != 0:
    print(0)
    exit()

cnt = (X + Y) // 3#移動した回数
move = abs(X-Y)#上　or 左に何回多く移動したか
if cnt > X or cnt > Y:
    print(0)
    exit()


new_x = X-cnt
# print(_up,_right,move)
#縦と横に何回移動したかわかったら、その組み合わせで解ける
ans = comb(cnt,new_x)
print(ans%mod)
