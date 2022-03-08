import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
"""
どうゆうときにテレポートするかを考える
次の街に行く際に歩くよりもテレポートのほうが楽なとき
"""
N,A,B = MI()
towns = LI()
ans = 0
for i in range(N-1):
    dist = towns[i+1] - towns[i]
    if dist*A < B:
        ans += dist*A
    else:
        ans += B
print(ans)
