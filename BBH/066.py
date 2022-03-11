import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = S()
AD = s.replace("BC","D")

a = 0
d = 0
for i in range(len(AD)):
    if AD[i] == "A":
        a += 1
    elif AD[i] == "B" or AD[i]=="C":
        a = 0
    else:
        d += a

print(d)
