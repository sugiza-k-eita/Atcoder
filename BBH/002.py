import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,K = MI()
ns = LI()
mod= 10**9+7
K %= mod
box = [[0]*2000 for i in range(2000)]
N_cnt = 0
cnt= 0
for i in range(N-1):
    for j in range(i+1,N):
        if ns[i] > ns[j]:
            N_cnt += 1
        if ns[i] != ns[j]:
            cnt += 1


innser_select = N*(N-1)//2
outer_select = K*(K-1)//2
innser_select %=mod
outer_select %=mod

tmp = cnt*outer_select
tmp%=mod
tmp2 = N_cnt *K
tmp2%=mod
ans = (tmp+tmp2)%mod
print(ans)
