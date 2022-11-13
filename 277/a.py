import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,X = MI()
P = LI()

for i in range(N):
    if P[i] == X:
        print(i+1)
        exit()
        
N,X = map(int,input().split())
P = list(int,input().split())
for i in range(N):
    if P[i] == X:
        print(i+1)
        exit()