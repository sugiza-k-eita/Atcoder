import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
import bisect

N, Q = MI()
box = []

a = []
for i in range(Q):
    T,A,B = MI()
    box.append(A)
    box.append(B)
    a.append([T,A,B])

box = list(set(box))
box.sort()
people = len(box)
node = [set() for i in range(people)]


for i in range(Q):
    T,A,B = a[i][0],a[i][1],a[i][2]
    a_ind = bisect.bisect_left(box,A)
    b_ind = bisect.bisect_left(box,B)
    if T == 1:
        node[b_ind].add(a_ind)
    if T == 2:
        node[b_ind].discard(a_ind)
    if T == 3:
        if a_ind in node[b_ind] and b_ind in node[a_ind]:
            print("Yes")
        else:
            print("No")
    
