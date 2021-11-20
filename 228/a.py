import sys
def LI(): return list(map(int, sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()


s, t, x = MI()
if s < t:
    if x >= s and x < t:
        print("Yes")
    else:
        print("No")
else:
    if x >= s or x < t:
        print("Yes")
    else:
        print("No")
