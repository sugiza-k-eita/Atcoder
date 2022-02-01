import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,L,W = MI()
ns = LI()
ns.sort()
head = 0
tail = 0
if ns[0] != 0:
    if ns[0]//W == ns[0]/W:
        head = ns[0]//W
    else:
        head =ns[0]//W + 1

if ns[-1] + W < L:
    nocover = L - ns[-1] - W
    if nocover //W == nocover/W:
        tail = nocover//W
    else:
        tail =nocover//W + 1

body = 0
for i in range(N-1):
    if ns[i] + W >= ns[i+1]:
        continue
    else:
        nocover = ns[i+1] - ns[i] - W
        if nocover //W == nocover/W:
            body += nocover//W
        else:
            body +=nocover//W + 1

print(head+body+tail)