"""
https://onlinejudge.u-aizu.ac.jp/solutions/problem/NTL_1_A/review/4920531/jakenu0x5e/Python3
計算量はn **1/4 試し割り法の√倍分速い
入力数が10**9以上ならロー法を使用する
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
r = []
s = [n]
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
    else:
        s.append(e // v)
        s.append(v)
r.sort()
print(str(n) + ":",*r)

