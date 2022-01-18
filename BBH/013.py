from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
N = II()
ns = S()

box = []
for i in range(0,10):    
    i = str(i)  
    for j in range(0,10):
        j = str(j)
        for k in range(0,10):
            k = str(k)
            pw = i+j+k
            box.append(pw)
ans = 0
for pw in box:
    cnt = 0
    for j in ns:
        if pw[cnt] == j:
            cnt += 1
        if cnt == 3:
            ans += 1
            break
print(ans)



