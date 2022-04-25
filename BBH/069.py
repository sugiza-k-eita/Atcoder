import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
num = []
for i in range(N):
    a = II()
    num.append(a)
num.sort()

if N % 2 == 0:
    lower = num[:N//2]
    upper = num[N//2:]
    upper_sum = sum(upper)*2 - upper[0]
    lower_sum = sum(lower)*2 - lower[-1]
elif N % 2 == 1:
    if N % 4 == 1:
        lower = num[:N//2+1]
        upper = num[N//2+1:]
        upper_sum = sum(upper)*2
        lower_sum = sum(lower)*2 - lower[-1] - lower[-2]

    elif N % 4 == 3:
        lower = num[:N//2]
        upper = num[N//2:]
        upper_sum = sum(upper)*2 - upper[0] - upper[1]
        lower_sum = sum(lower)*2
ans = upper_sum - lower_sum 
print(ans)
# print(lower,upper)
    