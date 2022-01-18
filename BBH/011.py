"""
AとBの公約数
→AとBの最大公約数の約数
"""
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

from math import gcd
A,B = MI()
c =gcd(A,B)
#計算量は√n
#入力値が10**9以上ならロー法を使用する
def tameshi(n):
  ret = []
  for i in range(2, int(n ** (1 / 2)) + 1):
    if i > n:break
    while n % i == 0:
      n //= i
      ret.append(i)
  if n != 1:
    ret.append(n)
  return ret

ans = tameshi(c)
print(len(set(ans))+1)

