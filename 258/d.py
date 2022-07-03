import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,X = MI()
box = []
time = 0
cnt = X

ans = float("inf")
for i in range(N):
    A,B = MI()
    # box.append([A,B,time,cnt])
    tmp = A  + time + B*cnt
    ans = min(ans,tmp)
    
    time += A+B
    cnt -= 1
    if cnt == -1:
        break
print(ans)
    
    