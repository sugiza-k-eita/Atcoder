import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,X = MI()
candies = LI()
box = []
for i in range(N-1):
    box.append(candies[i]+candies[i+1])
    
ans = 0
cnt = 0
for i in range(0,N-1):
    if box[i] > X:
        cnt = box[i] - X
        cut = min(candies[i+1],cnt)
        box[i] -= cut
        ans += cnt
        if i+1 < N-1:
            box[i+1] -= cut

print(ans)
# print(box)


        

