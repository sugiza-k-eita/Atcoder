import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()
B = LI()
hit = 0
blow = 0
for i in range(N):
    for j in range(N):
        if A[i] == B[j]:
            if i == j:
                hit += 1
            else:
                blow += 1

print(hit)
print(blow)