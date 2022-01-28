from collections import deque
import sys

from paramiko import SecurityOptions
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
from itertools import combinations,permutations

N = II()
ninzu = 2*N
box = [[None]*ninzu for i in range(ninzu)]
for xx in box:
    print(xx)
for i in range(ninzu-1):
    ns = LI()
    for j in range(len(ns)):
        box[i][j+i+1] = ns[j]

for xx in box:
    print(xx)


cnt = 0
for x in combinations(range(4), 2):
    cnt +=1
print(cnt)