import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

import string
box= list(string.ascii_lowercase)
d = {}
a = {}
for i in range(26):
    d[box[i]] = i
    a[i] = box[i]

letter = S()
cnt = II()
ans = ""
for s in letter[:-1]:
    if d[s] == 0:
        ans+= s
        continue
    plus= 26 - d[s]
    if cnt < plus:
        ans += s
        continue
    else:
        cnt -= plus
        ans += "a"

if cnt+d[letter[-1]] == 0:
    ans+=letter[-1]
else:
    tail = (cnt+d[letter[-1]])%26
    ans+= a[tail]
print(ans)

