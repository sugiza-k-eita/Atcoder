import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

x1,y1,x2,y2 = MI()

dist= (x1-x2)**2 + (y1-y2)**2

if dist > 20:
    print("No")
    exit()

box = [(2,1),(2,-1),(1,2),(1,-2),(-1,2),(-1,-2),(-2,1),(-2,-1)]
first = []
second = []

for i,j in box:
    ax,ay = x1+i,y1+j
    bx,by = x2+i,y2+j
    first.append([ax,ay])
    second.append([bx,by])

for f in first:
    for s in second:
        if f == s:
            print("Yes")
            exit()
print("No")