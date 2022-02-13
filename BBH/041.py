"""
a,b,cいずれもKの倍数or K//2の倍数である。
なので、場合分けをして計算する
"""

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N, K = MI()
odd_box = []
even_box = []
for i in range(K,N+1):
    if i%K == 0:
        odd_box.append(i)
# print(odd_box)


if K %2 == 0:
    for j in range(K//2,N+1):
        if j%(K//2) == 0 and j%K != 0:
            even_box.append(j)
# print(even_box)

print(len(even_box)**3 + len(odd_box)**3)