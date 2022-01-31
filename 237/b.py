import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
H,W = MI()

box =  []

for i in range(H):
    w = LI()
    box.append(w)
l_2d_t = [list(x) for x in zip(*box)]

for i in l_2d_t:
    print(*i, sep=" ")    