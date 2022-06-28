import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
import string
sys.setrecursionlimit(10 ** 6)

N,X = MI()
cnt = 0

box = list(string.ascii_uppercase)

while X > 0:
    X -= N
    cnt += 1
    if X <= 0:
        print(box[cnt-1])
        exit()
