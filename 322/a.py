import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = II()
s = S()

for i in range(N):
    if s[i-2] == "A" and s[i-1] == "B" and s[i] == "C":
        print(i-1)
        exit()
print(-1)