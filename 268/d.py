import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,M = MI()
Sbox = []
Tbox = []
for i in range(N):
    s = S()
    Sbox.append(s)
    

for j in range(M):
    t = S()
    Tbox.append(t)

print(Sbox)

