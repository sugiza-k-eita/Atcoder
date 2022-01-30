from collections import Counter
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
mod = 10**9 + 7

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

box = []

for i in range(1,N+1):
    yakusuu = tameshi(i)
    box += yakusuu

c = Counter(box)
ans = 1
for i in range(2,N+1):
    ans *= (c[i]+1)
    ans %= mod
print(ans)