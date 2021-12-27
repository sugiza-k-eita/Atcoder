from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,X =MI()
que= deque()
box = [[None] for i in range(N)]
for i in range(N):
  L,*a = MI()
  
  if i == 0:
    for x in a:
      if X//x == X/x:
        que.append(X//x)
  box[i] =a


for cnt in range(1,N):
  tmp_que = deque()
  while que:
    x = que.popleft()
    for i in box[cnt]:
      if x/i >= 1 and x//i == x/i:
        tmp_que.append(x//i)
  que = tmp_que

print(que.count(1))
  