import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
box = []
for i in range(N):
    x,y = MI()
    box.append([y,x])

lr = S()
a = []
for i in range(N):
    a.append([box[i][0],box[i][1],lr[i]])

a.sort()

for i in range(1,N):
    prenum,prex,prelr = a[i-1][0],a[i-1][1],a[i-1][2]
    num,x,lr = a[i][0],a[i][1],a[i][2]
    if prenum == num and prelr == "R" and lr == "L":
        print("Yes")
        exit()
print("No")