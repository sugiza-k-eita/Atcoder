import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

a,b = MI()

if b== 10:
    if a == 9 or a == 1:
        print("Yes")
        exit()

if a + 1 == b:
    print("Yes")
    exit()

print("No")