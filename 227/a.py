import sys
def MI(): return map(int, sys.stdin.readline().rstrip().split())


N, K, A = MI()
aa = K+A-1
cnt = 0
while True:
    cnt += 1
    aa = aa-1
    if aa == 1:
        break
ans = cnt % N
print(ans+1)
