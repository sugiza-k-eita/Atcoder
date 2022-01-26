import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

K,T= MI()
ns = LI()
goukei = sum(ns)
itiban = max(ns)
nokori = goukei - itiban
ans = max(itiban-nokori -1, 0)
print(ans)