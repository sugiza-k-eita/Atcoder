import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
ns = LI()
ruiseki =[0 for i in range(N)]
ruiseki[0] = ns[0]
for i in range(1,N):
    ruiseki[i] = ruiseki[i-1] + ns[i]
ruiseki = [0] + ruiseki
top= [0 for i in range(N)]
top[0] = max(ns)

for i in range(N):
    cnt = -1
    for j in range(i+1,N+1):
        cnt += 1
        top[cnt] = max(ruiseki[j] - ruiseki[i],top[cnt])

for i in top:
    print(i)