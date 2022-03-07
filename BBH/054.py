import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

X,Y,A,B,C = MI()
p = LI()
q = LI()
r = LI()
p.sort(reverse=True)
q.sort(reverse=True)
p = p[:X]
q = q[:Y]

pqr = p+q+r
pqr.sort(reverse=True)
aaa = pqr[:X+Y]
print(sum(aaa))