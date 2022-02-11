import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()   

N = II()
s = S()
s = s
black = [0 for i in range(N)]
white = [0 for i in range(N)]

for i in range(N):
    if s[i] == "#":
        black[i] = black[i-1] + 1
        white[i] = white[i-1]
    else:
        black[i] = black[i-1]
        white[i] = white[i-1] + 1
black = [0] + black
white = [0] + white
ans = 10** 18
# print(black,white)
for i in range(N+1):
    tmp = white[N] -white[i] + black[i]
    # print(tmp,white[N],white[i],black[i])
    ans = min(tmp,ans)
print(ans)