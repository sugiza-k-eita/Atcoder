import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

def power(x, y,mod = 10**9 +7):
    if y == 0:
        return 1
    elif y == 1:
        return x % mod
    elif y % 2 == 0:
        return power(x, y/2)**2 % mod
    else:
        return power(x, int(y/2))**2 * x % mod

mod = 10**9 +7
N,Q =MI()
ns = LI()
c = LI()
for i in range(Q):
    c[i] -= 1
c = [0] + c
box = [0 for i in range(N-1)]
ruiseki = [0 for i in range(N)]
for i in range(N-1):
    box[i] = power(ns[i],ns[i+1])


for i in range(1,N):
    ruiseki[i]+= (ruiseki[i-1] + box[i-1])%mod
distance = 0

for i in range(0,Q):
    tmp1,tmp2 = c[i],c[i+1]
    if tmp1 > tmp2:
        tmp1,tmp2 = tmp2,tmp1

    distance += (ruiseki[tmp2] - ruiseki[tmp1]) %mod

distance += ruiseki[c[-1]]
print(distance%mod)