import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
H = LI()
position = H[0]
for i in range(1,N):
    if position < H[i]:
        position = H[i]
        continue
    else:
        print(position)
        exit()

print(position)