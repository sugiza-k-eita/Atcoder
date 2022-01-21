import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
cnt = 0
A_cnt = 0
B_cnt = 0
AB_cnt =0
for i in range(N):
    s = S()
    for j in range(len(s)-1):
        if s[j] == "A" and s[j+1] == "B":
            cnt += 1
    
    if s[0] == "B":
        B_cnt += 1
    if s[-1] == "A":
        A_cnt += 1
    if s[0] == "B" and s[-1] == "A":
        AB_cnt += 1

if A_cnt == B_cnt == AB_cnt != 0:
    cnt -= 1
ans = min(A_cnt,B_cnt)
print(ans+cnt)

