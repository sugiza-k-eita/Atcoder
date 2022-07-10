import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import math
a,b,d = MI()

N_x = a*(math.cos(math.radians(d))) - b*(math.sin(math.radians(d)))
N_y = a*(math.sin(math.radians(d))) + b*(math.cos(math.radians(d)))
print(N_x,N_y)