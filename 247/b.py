import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
myoujibox = [[] for i in range(N)]
namebox = [[] for i in range(N)]

for i in range(N):
    s,t = map(str,input().split())
    myoujibox[i].append(s)
    namebox[i].append(t)

myouji = True
name = True
for i in range(N):
    for j in range(N):
        if i == j:
            continue

        if myoujibox[i] == myoujibox[j]:
            myouji = False
        elif myoujibox[i] == namebox[j]:
            myouji = False

        if namebox[i] == myoujibox[j]:
            name = False
        elif namebox[i] == namebox[j]:
            name = False
    
    if name == False and myouji == False:
        print("No")
        exit()
    else:
        myouji = True
        name = True
print("Yes")


