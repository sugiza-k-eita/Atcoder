import sys
from collections import deque
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M = MI()
first = [[] for i in range(N)]
second = [[] for i in range(N)]

for i in range(M):
    a,b = MI()
    a -= 1
    b -= 1
    first[a].append(b)
    first[b].append(a)

for i in range(M):
    c,d = MI()
    c -= 1
    d -= 1
    second[c].append(d)
    second[d].append(c)

leng_box1 = []
leng_box2 = []
index_f = 0
count_f = 0
index_s = 0
count_s = 0
for xx in range(N):
    leng1 = len(first[xx])
    leng2 = len(second[xx])
    if count_f < leng1:
        count_f = leng1
        index_f = xx
    if count_s < leng2:
        count_s= leng2
        index_s = xx
    leng_box1.append(leng1)
    leng_box2.append(leng2)

leng_box1.sort()
leng_box2.sort()

if leng_box1 != leng_box2:
    print("No")
    exit()


que1 = deque()
que1.append(index_f)
seen1 = [True]*N
seen1[index_f] = False
dist1 = [0]*N
dist1[index_f] = 1
while que1:
    node = que1.popleft()
    for nv in first[node]:
        if seen1[nv] == False:
            continue
        seen1[nv] = False
        dist1[nv] += dist1[node] + 1
        que1.append(nv)
ans1 = sum(dist1)


que2 = deque()
que2.append(index_s)
seen2 = [True]*N
seen2[index_s] = False
dist2 = [0]*N
dist2[index_s] = 1
while que2:
    node = que2.popleft()
    for nv in second[node]:
        if seen2[nv] == False:
            continue
        seen2[nv] = False
        dist2[nv] += dist2[node] + 1
        que2.append(nv)
ans2 = sum(dist2)

if ans2 == ans1:
    print("Yes")
else:
    print("No")
