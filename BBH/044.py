"""
不親切の人のいいことは無視していい
正直者の言うことは全部正しい
"""

from itertools import product
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
box = []
for i in range(N):
    A = II()
    tmp = dict()
    for j in range(A):
        x,y = MI()
        x -= 1
        tmp[x]=y
    box.append(tmp)
"""
y= 1は正直者、x=0は不親切
"""
ans = 0
for flg in product([0,1],repeat=N):
    a = True
    for i in range(N):
        if flg[i] == 0:
            continue
        for j in box[i]:
            if box[i][j] != flg[j]:
                a = False
                break
        if a == False:
            break
    if a == True:
        ans = max(ans,sum(flg))
print(ans)