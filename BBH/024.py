import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
box = []
for i in range(N):
    x,l = MI()
    head = x-l
    tail = x+l
    box.append([head,tail])
    
box.sort(key = lambda x: x[1])
leng = box[0][1]
cnt = 1
for i in range(1,N):
    if box[i][0] < leng:
        continue
    else:
        leng = box[i][1]
        cnt += 1
print(cnt)


