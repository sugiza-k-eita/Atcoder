from asyncore import loop
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

"""
a%b >= K となる個数を求める
1 < a < N
1 < b < N

b についてloop

0%b, 1%b, 2%b, ・・・N%b
の数列について考える
0,1,2・・・b-1,0,1, ・・・,r
N = p*b + r
(pは繰り返される0~b-1の回数, rは繰り返されず余ったやつ)
・pについて
    0,1,2,・・・b-1の中に何個K以上があるか
・rについて
    0,1,2 ・・・rについて何個K以上があるか
"""
N,K = MI()
ans = 0
if K == 0:
    print(N**2)
    exit()

for b in range(K+1,N+1):
    p = N//b
    #商
    r = N - p*b
    #あまり
    
    #1,2・・・b-2,b-1,0,1,2という1周期の中にK以上の数は何個あるか？
    one_loop = b-K
    #b-kでkよりも大きい数なので、以上出会ったら+1
    loops = one_loop*p
    #one_loopという変数には、1周期にK以上の数が出てくる個数なので、その周期がp回
    amari = max(r-K+1,0)
    # print(b,p,r,one_loop,loops)
    ans += loops + amari
    
print(ans)