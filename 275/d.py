from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from functools import lru_cache
@lru_cache
def f(n):
    if n == 0:
        return 1
    return f(n//2)+f(n//3)

N = II()
print(f(N))