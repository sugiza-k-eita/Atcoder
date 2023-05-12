import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,T  = MI()
C = LI()
R = LI()

box = []
if T in C:
    for i in range(N):
        if C[i] == T:
            box.append([R[i],i])
    box.sort()
    print(box[-1][1]+1)


else:
    for i in range(N):
        if C[i] == C[0]:
            box.append([R[i],i])
    box.sort()
    print(box[-1][1]+1)
