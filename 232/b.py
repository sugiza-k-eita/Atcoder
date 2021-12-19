import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
import string
a1 = list(string.ascii_lowercase)*2
a2 = list(string.ascii_lowercase)*2

d = {}
for i in range(26):
    d[a1[i]] = i


s = S()
t =S()
head1 = d[s[0]]
head2 = d[t[0]]

use1 = a1[head1:head1+26]
use2 = a2[head2:head2+26]
number = []
number2 = []


# print(use1)
# print(use2)

for x in range(len(s)):
    tmp = use1.index(s[x])
    tmp2= use2.index(t[x])
    if tmp == tmp2:
        continue
    else:
        print("No")
        exit()


print("Yes")
