from collections import Counter
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
ns = LI()

c = Counter(ns)
if N %2 == 1:
    #奇数の時
    if c[0] != 1:
        print(0)
        exit()
    for i in range(2,N+1,2):
        if c[i] != 2:
            print(0)
            exit()


if N %2 == 0:
    #偶数の時
    for i in range(1,N+1,2):
        if c[i] != 2:
            print(0)
            exit()

iter = N//2
mod = 10**9 + 7
print(2**iter%mod)