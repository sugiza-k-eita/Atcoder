import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,X = MI()
s = S()
cnt = X-1
for i in range(N):
    letter = s[i]
    if letter == "U":
        cnt = (cnt-1)//2
    elif letter == "L":
        cnt = 2*cnt + 1
    elif letter == "R":
        cnt = 2*cnt + 2
print(cnt+1)
