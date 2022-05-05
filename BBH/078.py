import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

s = S()
num = II()
box = []
for i in range(len(s)):
    for j in range(1,6):
        if i + j > len(s):
            break
        box.append(s[i:i+j])

box = set(box)
ns = sorted(box)
# print(ns)
print(ns[num-1])

