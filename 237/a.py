import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N= II()
lr = S()
box = [0]
pred = 0
if lr[0] == "L":
    box.insert(0,1)
    pred = 0
else:
    box.insert(1,1)
    pred = 1

for i in range(1,N):
    if lr[i] == "L":

