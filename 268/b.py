import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s =S()
t = S()

len_s = len(s)
len_t = len(t)

if len_s > len_t:
    print("No")
    exit()

if s == t[:len_s]:
    print("Yes")
else:
    print("No")