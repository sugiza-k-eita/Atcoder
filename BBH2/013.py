from collections import deque
import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
N = II()
ns = S()

box = []
for i in range(0,10):    
    i = str(i)  
    for j in range(0,10):
        j = str(j)
        for k in range(0,10):
            k = str(k)
            pw = i+j+k
            box.append(pw)
ans = 0
for pw in box:
    cnt = 0
    for j in ns:
        if pw[cnt] == j:
            cnt += 1
        if cnt == 3:
            ans += 1
            break
print(ans)


"""
000~999の並びについて全探索
sについて全探索すると、同じ数列を数える可能性がある

ex)
0224の場合
2文字目を消すと、024となる
1文字目を消すと、024となる
この場合は、同じ数列を数えてしまう。

しかし、000~999の並びについて全探索すれば、同じpwを数えることがないです。

そのため、000~999の並びについて全探索し、ネストする形で、sについて前から探索
一致したら、その数列についての全探索をおえ、ans += 1
一致しなかったら、そのまま
"""