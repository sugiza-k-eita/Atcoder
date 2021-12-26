import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

X,Y = MI()

if X >= Y:
    print(0)
else:
    ans = (Y-X-1)//10 + 1
    print(ans)