import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
ns = LI()
ns.sort()

cnt = 0
tmp_max = ns[0]
for i in range(1,N):
    if tmp_max *2 >= ns[i]:
        tmp_max += ns[i]
    else:
        cnt = i
        tmp_max += ns[i]

print(N-cnt)