from math import gcd
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

L,R = MI()
if gcd(R,L) == 1:
    print(R-L)
    exit()

for i in range(L,R):
    if gcd(R,i) == 1:
        ans = R -i
        break
    else:
        continue

for i in range(R,L,-1):
    if gcd(i,L) == 1:
        ans2 =i-L
        break
    else:
        continue
aa = max(ans,ans2)
a = L
b = R
ans3 = 0
for w in range(R-L,aa,-1):
    for l in range(L,R):
        r = l + w
        if r >= R:
            break

        if gcd(l,r) == 1:
            print(r-l)
            exit()
print(aa)




    
