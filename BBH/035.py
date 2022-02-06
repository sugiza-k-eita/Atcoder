import bisect
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,H = MI()
binta = 0
throw= []
binta_cnt = 0
throw_cnt = 0
for i in range(N):
    a,b = MI()
    binta = max(binta,a)
    throw.append(b)

throw.append(binta)
throw.sort()

index = bisect.bisect_right(throw,binta)

use_patan = throw[index-1:]

use_patan.reverse()
life = H
for i in range(len(use_patan)-1):
    life -= use_patan[i]
    if life <= 0:
        print(i+1)
        exit()
    throw_cnt = i+1

if life//use_patan[-1] == life/use_patan[-1]:
    binta_cnt = (life//use_patan[-1])
elif life//use_patan[-1] != life/use_patan[-1]:
    binta_cnt = (life//use_patan[-1]) + 1

print(binta_cnt+throw_cnt)
