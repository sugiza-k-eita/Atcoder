import sys
from itertools import combinations
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

def two_distance(x1,y1,x2,y2):
    if x1 > x2:
        x1,x2 = x2,x1
    if y1 > y2:
        y1,y2 = y2,y1
    tmp_x = (x2-x1)**2
    tmp_y = (y2 -y1)**2
    distance = (tmp_x + tmp_y)**0.5
    return distance

N,M = MI()
box = [[] for i in range(N+M)]
for i in range(N):
    x,y,r = MI()
    box[i] = [x,y,r]

for j in range(M):
    x,y = MI()
    box[N+j] = [x,y]

ans = 100
for i,j in combinations(range(N+M),2):
    x1,y1,x2,y2 = box[i][0],box[i][1],box[j][0],box[j][1]
    tmp_ans = two_distance(x1,y1,x2,y2)
    r =tmp_ans/ 2
    if i < N and j < N:
        ans = min(ans,box[i][2],box[j][2])
    if i < N:
        ans = min(ans,box[i][2], tmp_ans-box[i][2])
    else:
        ans = min(ans,r)

print(ans)