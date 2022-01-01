"""
https://onlinejudge.u-aizu.ac.jp/solutions/problem/NTL_1_A/review/4920531/jakenu0x5e/Python3
"""

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

def gcd(m, n):
    while n:
        m, n = n, m % n
    return m
    #最大公約数

def pollard_rho(n, a, x0):
    f = lambda x: (x**2 + a) % n
    x = y = ys = x0; r = 1; q = 1
    m = 100
    d = 1
    while d == 1:
        x = y
        for i in range(r):
            y = f(y)
        for k in range(0, r, m):
            ys = y
            for i in range(min(m, r-k)):
                y = f(y)
                q = q * abs(x - y) % n
            d = gcd(q, n)
            if d != 1:
                break
        r <<= 1
    if d == n:
        while d == 1:
            ys = f(ys)
            d = gcd(abs(x - ys), n)
    return d if d < n else -1
import random
random.seed()

n = II()
#nは素因数分解したい数
r = []
#素因数を格納する箱
s = [n]
#素因数分解をしたい数を格納
while s:
    e = s.pop()
    for i in range(10):
        a = random.randint(1, e-1)
        x0 = random.randint(1, e-1)
        v = pollard_rho(e, a, x0)
        if v != -1:
            break
    if v == -1:
        r.append(e)
        #-1になったら、その数は素因数ということなので、rに格納
    else:
        s.append(e // v)
        s.append(v)
        #そうではないときは、その数を改めて素因数分解をする
r.sort()
print(str(n) + ":",*r)

