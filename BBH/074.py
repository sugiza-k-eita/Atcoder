import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
box = []
for i in range(N):
    a = II()
    box.append(a)

sum_box = sum(box)
if sum_box %2 == 0:
    for i in box:
        if i%2 == 0:
            continue
        else:
            print("first")
            exit()
    print("second")

else:
    print("first")
        