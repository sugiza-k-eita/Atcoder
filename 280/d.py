import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

K = II()
def tameshi(n):
    ret = []
    for i in range(2, int(n ** (1 / 2)) + 1):
        if i > n:break
        while n % i == 0:
            n //= i
            ret.append(i)
    if n != 1:
        ret.append(n)
    return ret

a = tameshi(K)
maximun = 0

import collections
c = collections.Counter(a)
# print(c)
set_a = list(set(a))
# print(set_a)

def cal(x,y,cnt,check):
    if x < y:
        cnt += y//x
        check += 1
        cal(x,y,cnt,check)
    return cnt

flg = []
for i in range(len(set_a)):
    cnt = 0
    minus = cal(set_a[i],c[set_a[i]],cnt,1)
    print(set_a[i],c[set_a[i]],minus)
    z = set_a[i]*(c[set_a[i]]-minus)
    maximun = max(z,maximun)
print(maximun)