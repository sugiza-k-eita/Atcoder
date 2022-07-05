import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,X = MI()
A = LI()
sum_box = []
for i in range(N-1):
    sum_box.append(A[i]+A[i+1])
    
ans = 0
cnt = 0
for i in range(0,N-1):
    if sum_box[i] > X:
        cnt = sum_box[i] - X
        cut = min(A[i+1],cnt)
        sum_box[i] -= cut
        ans += cnt
        if i+1 < N-1:
            sum_box[i+1] -= cut

print(ans)
# print(sum_box)


        

