import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,K = MI()
s = S()

"""
RR or LL のところは切り離すことなく、一つのものとして考える
なぜなら、切り離すと幸福度が下がるため

今回は連続しているところは一つと考え、RLRL or LRLRの文字列が最小になるようにする
N - L or R の種類
が幸福度


K回の操作で増える数は最大で2 端の場合のみ1 それ以外は0 or -2
LR RL
RL LR の場合のときは+2
"""
ns = s[0]
for i in range(1,N):
    if ns[-1] == s[i]:
        continue
    else:
        ns += s[i]

if ns[-1] == s[-1]:
    pass
else:
    ns += s[-1]
if len(ns) % 2 == 0:
    ans = N-len(ns) + min(len(ns)//2,K)*2
else:
    ans = N-len(ns) + min(len(ns)//2+1,K)*2
print(min(ans,N-1))
        
    

        
        

