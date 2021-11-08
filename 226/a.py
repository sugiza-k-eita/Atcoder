import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


X, a = input().split(".")
X = int(X)
flg = int(a[0])
if flg >= 5:
    print(X+1)
else:
    print(X)
