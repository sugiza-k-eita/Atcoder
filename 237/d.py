import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N= II()
lr = "#"+ S()
box = [[-1] for i in range(N+1)]
l_cnt = 0
r_cnt = N

for i in range(1,N+1):
    if lr[i] == "L":
        box[r_cnt] = i-1
        r_cnt -= 1
    else:
        box[l_cnt] = i-1
        l_cnt += 1

ind = box.index([-1])
box[ind] = N
print(*box, sep=" ")