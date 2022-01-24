import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

s = S()
box = []
for i in s:
    box.append(i)

n,m = MI()
n -= 1
m -= 1

tmp = box[n]
box[n] = box[m]
box[m] = tmp
print(*box,sep="")