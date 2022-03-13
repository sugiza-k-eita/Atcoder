import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

V,A,B,C = MI()
cnt = 1

while V >=  0:
    if cnt %3 == 1:
        V -= A
        if V < 0:
            print("F")
            exit()
    elif cnt %3 == 2:
        V -= B
        if V < 0:
            print("M")
            exit()
    elif cnt %3 == 0:
        V -= C
        if V < 0:
            print("T")
            exit()
    cnt += 1
    # print(V)
