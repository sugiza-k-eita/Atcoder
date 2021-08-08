"""
今回は、nの上限が3*10**5なので、for文を1回しか回せない
しかし、A_i,A_jの２つに対して、計算しなければならない
なので、A_jを固定して、A_iを 0~A_j-1までとするか
別の方法でfor文を回す必要がある
今回は、Aの幅が200なので、AについてのCountしてfor文を回す
"""
from collections import Counter

n = int(input())
ns = list(map(int, input().split()))
cnt = Counter(ns)
ans = 0

for x in range(-200, 201):
    for y in range(x+1, 201):
        cx = cnt[x]
        cy = cnt[y]
        ans += cx*cy*(x-y)**2
print(ans)
