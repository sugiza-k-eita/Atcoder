import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,K = MI()
s = S()
cnt = 0

if N == 1:
    print(1)
    exit()
    

box = []
for i in range(N-1):
    if s[i] == s[i+1]:
        cnt += 1
    else:
        cnt +=1
        box.append(cnt)
        cnt = 0

if s[-2] == s[-1]:
    cnt += 1
    box.append(cnt)
else:
    cnt = 1
    box.append(cnt)


ruiseki = [0,0]
for i in box:
    ruiseki.append(ruiseki[-1]+i)

ruiseki.append(ruiseki[-1])

if len(ruiseki)-3 <= 2*K:
    print(N)
    exit()

ans = 0
if s[0] == "0":
    start = 0
else:
    start = 1



width = 2*K+1
for l in range(start,len(ruiseki)-1,2):
    r = l + width
    if r >= len(ruiseki):
        break
    # print(l,r)
    tmp_ans = ruiseki[r]-ruiseki[l]
    ans = max(ans,tmp_ans)
    
print(ans)