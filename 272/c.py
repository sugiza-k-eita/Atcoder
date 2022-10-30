import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
A = LI()

odd = [-10**9,-10**9]
even = [-10**9,-10**9]

for a in A:
    if a%2 == 0:
        even.append(a)
    else:
        odd.append(a)

even.sort()
odd.sort()

ans = max(even[-1]+even[-2],odd[-1]+odd[-2])
if ans < 0:
    print(-1)
else:
    print(ans)