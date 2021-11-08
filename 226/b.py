import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


N = II()
box = [S() for _ in [None]*(N)]
ans = set(box)
print(len(ans))
