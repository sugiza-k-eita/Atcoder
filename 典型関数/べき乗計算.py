"""
https://atcoder.jp/contests/abc228/tasks/abc228_e
M**(K**N)を求める問題
がしかし計算量が爆発しちゃうからそれを頑張る
"""

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,K,M = MI()
MOD = 998244353

def solve(N, K, M):
   if M % MOD == 0:
      return 0
   nseq = pow(K, N, MOD-1)
   #フェルマーの定理よりK**Nはnseqである
   res = pow(M, nseq, MOD)
   #フェルマーの定理よりM**nseqはresである
   return res


res = solve(N, K, M)
print(res)


