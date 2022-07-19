import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()

minus_cnt = 0
for i in range(N):
    if A[i] < 0:
        minus_cnt += 1
        A[i] *= -1

        

if minus_cnt % 2 == 0:
    print(sum(A))
else:
    print(sum(A)-min(A)*2)