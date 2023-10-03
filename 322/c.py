import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N,M = MI()
A = LI()

days = [0 for i in range(N)]
cnt = 0
for i in range(N):
    if i == A[cnt]-1:
        cnt += 1
        days[i] = 1

# print(days)
ans = [0 for i in range(N)]

left = 0
for right in range(N):
    if days[right] == 1:
        for i in range(right-left):
            ans[left+i] = right - left-i
        left = right+1


print('\n'.join(map(str, ans)))