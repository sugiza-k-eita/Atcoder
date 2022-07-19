import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = S()

if s[0] == s[1] == s[2]:
    print(-1)

else:
    if s[0] == s[1]:
        print(s[2])

    elif s[0] == s[2]:
        print(s[1])
    else:
        print(s[0])