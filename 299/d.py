import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = II()
box = []
left,right = 0,N-1
for i in range(5):
    middle = (left+right)//2
    print("?"+" "+str(middle))
    print()
    flg = II()
    if flg == 0:
        left = middle
    else:
        right = middle
    box.append([middle,flg])
box.sort()
for i in range(len(box)-1):
    if box[i][0]+1 ==box[i+1][0] and box[i][1] != box[i+1][1]:
        print(box[i][0]+1)