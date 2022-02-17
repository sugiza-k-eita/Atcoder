"""
個数制限のないナップサック問題
"""

import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

H,N = MI()
box = []
for i in range(N):
    damage,magic = MI()
    efficiency = damage/magic
    box.append([efficiency,magic,damage])

box.sort(reverse=True)
maxvalue_magic=box[0][1]


