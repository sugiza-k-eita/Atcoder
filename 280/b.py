import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()
ans_box = [A[0]]
flg = A[0]
for i in range(1,N):
    ans = A[i] - flg
    ans_box.append(ans)
    flg = A[i]
print(*ans_box, sep=" ")