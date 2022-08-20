import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


R,C = MI()

R -= 1
C -= 1

b = "black"
w = "white"
if R == 0 or R == 14:
    print(b)

elif R == 1 or R == 13:
    if C == 0 or C == 14:
        print(b)
    else:
        print(w)

elif R == 2 or R == 12:
    if C == 1 or C == 13:
        print(w)
    else:
        print(b)

elif R == 3 or R == 11:
    if C == 0 or C == 14 or C == 2 or C == 12:
        print(b)
    else:
        print(w)

elif R == 4 or R == 10:
    if C == 1 or C == 13 or C == 3 or C == 11:
        print(w)
    else:
        print(b)

elif R == 5 or R == 9:
    if C == 0 or C == 14 or C == 2 or C == 12 or C == 4 or C == 10:
        print(b)
    else:
        print(w)

elif R == 6 or R == 8:
    if C == 1 or C == 13 or C == 3 or C == 11 or C == 5 or C == 9:
        print(w)
    else:
        print(b)

elif R == 7:
    if C == 0 or C == 14 or C == 2 or C == 12 or C == 4 or C == 10 or C == 6 or C == 8:
        print(b)
    else:
        print(w)