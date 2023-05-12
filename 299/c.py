import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 7)

N = II()
letter = S()
ans = 0

o_cnt = 0
bar_cnt = 0
for i in range(N):
    if letter[i] == "o":
        o_cnt += 1
    else:
        bar_cnt += 1

if o_cnt == N or bar_cnt == N:
    print(-1)
    exit()

left = 0
for i in range(N):
    if letter[i] == "-":
        left = i
        break
for right in range(N):
    if letter[right] == "o":
        continue
    else:
        ans = max(ans,right-left)
        left = right

right = 0
for i in range(N-1,-1,-1):
    if letter[i] == "-":
        right = i
        break
for left in range(N-1,-1,-1):
    if letter[left] == "o":
        continue
    else:
        ans = max(ans,right-left)
        right = left
print(ans-1)




