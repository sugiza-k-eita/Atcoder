import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = S()
box = [0]
for i in range(len(s)-1):
    if s[i] == "0":
        box.append("0")
    else:
        box.append("1")

print(*box,sep="")