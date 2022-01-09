import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()

box = [0 for i in range(1000002)]
for i in range(N):
    a,b = MI()
    box[a] += 1
    box[b+1] -= 1

for i in range(1,1000002):
    box[i] += box[i-1]
print(max(box))