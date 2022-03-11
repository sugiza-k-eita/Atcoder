import sys
from itertools import product
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,K= MI()
ns = LI()
num = [0,1,2,3,4,5,6,7,8,9]

for i in range(10):
    if i in ns:
        num.remove(i)
str_num = str(N)
le = len(str_num)

for i in product(num,repeat = le):
    a = ""
    for j in i:
        a += str(j)
    if int(a) >= N:
        print(int(a))
        exit()
    
for i in product(num,repeat = le+1):
    a = ""
    for j in i:
        a += str(j)
    if int(a) >= N:
        print(int(a))
        exit()
