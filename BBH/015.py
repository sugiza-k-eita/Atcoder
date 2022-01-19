import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
ns = LI()
B = 0
cnt = 0
for i in range(N):
    if ns[i] <0:
        cnt +=1
        
ans = 0
box = []
for i in ns:
    ans += abs(i)
    box.append(abs(i))
box.sort()

if cnt %2 !=0:
    ans -= 2*box[0]
print(ans)