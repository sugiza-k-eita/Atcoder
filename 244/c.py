import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
box = [i for i in range(1,2*N+2)]

while True:
    x = box.pop()
    print(x, flush=True)
    if len(box) == 0:
        exit()
    y = II()
    if y == 0:
        exit()
    else:
        box.remove(y)
