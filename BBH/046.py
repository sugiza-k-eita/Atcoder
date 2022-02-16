import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

letter = S()

leng = len(letter)
ans = 0
T_cnt = 0
S_cnt = 0
for i in range(leng):
    if letter[i] == "T":
        if S_cnt <= 0:
            ans += 1
        else:
            S_cnt -= 1
    else:
        S_cnt += 1
ans += S_cnt
print(ans)