import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,M = MI()
s = S()
t = S()

flg1 = False
flg2 = False
if s == t[:N]:
    flg1 = True


if s == t[-N:]:
    flg2 = True


if flg1 == True and flg2 == True:
    print(0)
elif flg1 == True and flg2 == False:
    print(1)
elif flg1 == False and flg2 == True:
    print(2)
else:
    print(3)