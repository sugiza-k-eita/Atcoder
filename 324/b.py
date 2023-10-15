import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = II()

while True:
    if N %2 == 0:
        N = N//2
    else:
        break


while True:
    if N %3 == 0:
        N = N//3
    else:
        break
if N == 1:
    print("Yes")
else:
    print("No")