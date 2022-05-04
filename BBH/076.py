import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from itertools import product

s = S()
loop = len(s) - 1

ans = 0
for lo in product([0,1],repeat=loop):
    tmp_sum = 0
    letter = s[0]
    for i in range(loop):
        if lo[i] == 0:
            letter += s[i+1]
        else:
            tmp_sum += int(letter)
            letter = s[i+1]
    
    tmp_sum += int(letter)
    ans += tmp_sum
    
    
            
print(ans)

