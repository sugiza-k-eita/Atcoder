import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N,M = MI()
s = list(map(str,input().split()))
t = list(map(str,input().split()))
flg = [False]*N
cnt = 0
for i in range(N):
    if s[i] == t[cnt]:
        flg[i] = True
        cnt += 1
    else:
         continue

for a in flg:
    if a == True:
        print("Yes")
    else:
        print("No")

