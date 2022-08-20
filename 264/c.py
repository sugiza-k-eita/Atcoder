import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from itertools import product

H1,W1 = MI()
A = []
B = []
for i in range(H1):
    tmp = LI()
    A.append(tmp)

H2,W2 = MI()
for i in range(H2):
    tmp = LI()
    B.append(tmp)


for bits in product([0,1],repeat=H1+W1):
    Hbits = bits[:H1]
    Wbits = bits[H1:]
    if sum(Hbits) != H2 or sum(Wbits) != W2:
        continue
        
    C = A.copy()
    
    for i in range(H1-1,-1,-1):
        if Hbits[i] == 0:
            if len(C) == 0:
                break
            C.pop(i)
    
    l_2d_t = [list(x) for x in zip(*C)]
    for i in range(W1-1,-1,-1):
        if Wbits[i] == 0:
            if len(l_2d_t) == 0:
                break
            l_2d_t.pop(i)
    
    final = [list(x) for x in zip(*l_2d_t)]
    
    if final == B:
        print("Yes")
        exit()
print("No")