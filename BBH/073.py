import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()

box = [1]
a = 1
while True:
    a *= 6
    if a > 100000:
        break
    else:
        box.append(a)
a = 1
while True:
    a *= 9
    if a > 100000:
        break
    else:
        box.append(a)
    
box.sort()

dp = [0 for i in range(N+1)]
#引き出す金額(N) と　ひきだせる金額の種類でdp
for i in range(N+1):
    dp[i] = i

for i in range(1,N+1):
    for j in box:
        if i >= j:
            dp[i] = min(dp[i],dp[i-j]+1)
        else:
            break

print(dp[-1])


