import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
import collections
N = II()
box= []
for i in range(N):
    s = S()
    box.append(s)
print(max(box,key=box.count))
