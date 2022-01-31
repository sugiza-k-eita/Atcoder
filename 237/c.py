from collections import Counter
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

s = S()
leng = len(s)
head = 0
tail = 0

for i in range(leng):
    if s[i] == "a":
        head += 1
    else:
        break

for j in range(leng):
    if s[leng -j -1] == "a":
        tail += 1
    else:
        break
if tail - head > 0:
    aaa = "a"*(tail - head) +s
else:
    aaa = s

leng = len(aaa)
cnt = 0
for x in range(leng//2):
    if aaa[x] == aaa[leng-x-1]:
        cnt += 1
        continue

if cnt == leng//2:
    print("Yes")
else:
    print("No")


