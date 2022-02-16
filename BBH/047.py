from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

K = II()
if K < 10:
    print(K)
    exit()


cnt = 9
que = deque()
merge_list = [[] for i in range(10)]
for i in range(10):
    if i != 0:
        merge_list[i].append(i-1) 
    merge_list[i].append(i)
    if i != 9:
        merge_list[i].append(i+1)

for i in range(1,10):
    que.append(i)

while True:
    x = que.popleft()
    x = str(x)
    tail = x[-1]
    for m in merge_list[int(tail)]:
        new_x = str(x) + str(m)
        new_x = int(new_x)
        cnt += 1
        que.append(new_x)
        # print(que)
        if cnt == K:
            print(new_x)
            exit()

        