import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,M = MI()
A =LI()
B =LI()

for i in range(M):
    if B[i] in A:
        A.remove(B[i])
    else:
        print("No")
        exit()
print("Yes")