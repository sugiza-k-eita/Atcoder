import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

A,B,C,X = MI()

if X <= A:
    print(1)
    exit()

elif A < X and X <= B:
    bosuu = B-A
    t = C
    print(C/bosuu)
else:
    print(0)