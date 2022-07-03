import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
box = [[0] * 2*N for _ in range(2*N)]
for i in range(N):
    A = S()
    for j in range(N):
        box[i][j] = A[j]
        # box[i][j+N] = A[j]
        # box[i+N][j] = A[j]
        # box[i+N][j+N] = A[j]

mod = N
ans = 0
for s_x in range(N):
    for s_y in range(N):
        #右
        tmp = ""
        for i in range(N):
            s_x += 1
            s_x %= mod
            tmp += str(box[s_x][s_y])
        ans = max(ans,int(tmp))
        
        #左
        tmp = ""
        for i in range(N):
            s_x -= 1
            s_x %= mod
            tmp += str(box[s_x][s_y])
        ans = max(ans,int(tmp))
        
        #下
        tmp = ""
        for i in range(N):
            s_y += 1
            s_y %= mod
            tmp += str(box[s_x][s_y])
        ans = max(ans,int(tmp))
        
        #上
        tmp = ""
        for i in range(N):
            s_y -= 1
            s_y %= mod
            tmp += str(box[s_x][s_y])
        ans = max(ans,int(tmp))
        
        #右上
        tmp = ""
        for i in range(N):
            s_x += 1
            s_y += 1
            s_x %= mod
            s_y %= mod
            tmp += str(box[s_x][s_y])
        ans = max(ans,int(tmp))
        
        #左
        tmp = ""
        for i in range(N):
            s_x += 1
            s_y -= 1
            s_x %= mod
            s_y %= mod
            tmp += str(box[s_x][s_y])
        ans = max(ans,int(tmp))
        
        #下
        tmp = ""
        for i in range(N):
            s_x -= 1
            s_y += 1
            s_x %= mod
            s_y %= mod
            tmp += str(box[s_x][s_y])
        ans = max(ans,int(tmp))
        
        #上
        tmp = ""
        for i in range(N):
            s_x -= 1
            s_y -= 1
            s_x %= mod
            s_y %= mod
            tmp += str(box[s_x][s_y])
        ans = max(ans,int(tmp))
print(ans)