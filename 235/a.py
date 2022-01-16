import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

ns = S()
a = int(ns[0])
b = int(ns[1])
c = int(ns[2])

tmp = a+b+c
ans = tmp*100+tmp*10 +tmp
print(ans)