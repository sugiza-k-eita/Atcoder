import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

K = II()
hour = 21
if K >= 60:
    hour = 22
    K -= 60
if K < 10:
    m = "0" + str(K)
else:
    m = str(K)

print(str(hour)+":"+m)