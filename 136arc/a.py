import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
a = S()
z = []
for i in range(N):
    z.append(a[i])

"""
Cがあったらそこで切れる
BA→ABに帰ることができる
BB→Aにする
"""

ans = []
cnt = 0

while True:
    if z[cnt] == "A":
        ans.append("A")
    
    elif z[cnt] == "B":
        if cnt+1 == N:
            #最後がBのときは
            ans.append("B")
            break

        if z[cnt+1] == "A":
            z[cnt+1] = "B"
            z[cnt] = "A"
            ans.append("A")
    
        elif z[cnt+1] == "B":
            ans.append("A")
            cnt += 1
        else:
            ans.append("B")
    
    else:
        ans.append("C")
    cnt += 1
    
    if cnt >= N:
        break

print(*ans,sep="")


