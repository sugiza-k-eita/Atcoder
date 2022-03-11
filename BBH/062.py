import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

"""
縦、横わけて考える
縦横それぞれは尺取法でやれば2000**2に収まる
その後、たて＋よこ-1(-1は重複部分)を求め答えを出す。
"""

H,W = MI()
box= [[] for i in range(H)]
for i in range(H):
    box[i] = S()
t_box = list(zip(*box))
wlamp = [[0]*W for i in range(H)]
hlamp = [[0]*H for i in range(W)]

for i in range(H):
    cnt = 0
    for j in range(W):
        if box[i][j] == ".":
            cnt += 1
        elif box[i][j] == "#":
            for k in range(j-1,j-cnt-1,-1):
                wlamp[i][k] = cnt
            cnt = 0
        box[i][j] == 0
        
        if j == W-1 and box[i][-1] == ".":
            for k in range(-1,-(1+cnt),-1):
                wlamp[i][k] = cnt

for i in range(W):
    cnt = 0
    for j in range(H):
        if t_box[i][j] == ".":
            cnt += 1
        elif t_box[i][j] == "#":
            for k in range(j-1,j-cnt-1,-1):
                hlamp[i][k] = cnt
            cnt = 0
        t_box[i][j] == 0
        
        if j == H-1 and t_box[i][-1] == ".":
            for k in range(-1,-(1+cnt),-1):
                hlamp[i][k] = cnt

ans = 0
for i in range(H):
    for j in range(W):
        tmp = wlamp[i][j]+hlamp[j][i]
        ans = max(ans,tmp)

print(ans-1)