from operator import mod
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,Q = MI()
s = S()
head = 0
for i in range(Q):
    a,b = MI()
    b -= 1
    if a == 1:
        head += (N - b-1) % N
    else:
        print(s[(head+b)%N])