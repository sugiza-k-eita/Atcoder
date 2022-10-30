import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

box = []
porn_cnt = []
for i in range(9):
    a = S()
    for j in range(9):
        if a[j] == "#":
            porn_cnt.append([i,j])
    box.append(a)

# print(porn_cnt)

import itertools
ans = 0
for comb_4  in itertools.combinations(porn_cnt,4):
    a,b = comb_4[0][0],comb_4[0][1]
    c,d = comb_4[1][0],comb_4[1][1]
    e,f = comb_4[2][0],comb_4[2][1]
    g,h = comb_4[3][0],comb_4[3][1]
    hen1 = (c-a)**2 + (d-b)**2
    hen2 = (e-a)**2 + (f-b)**2
    hen3 = (c-g)**2 + (d-h)**2
    hen4 = (e-g)**2 + (f-h)**2
    taikakaku1 = (a-g)**2 + (b-h)**2
    taikakaku2 = (c-e)**2 + (d-f)**2
    if hen1 == hen2 == hen3 == hen4 and taikakaku1 == taikakaku2:
        ans += 1
print(ans)