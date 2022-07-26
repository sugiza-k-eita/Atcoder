import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

A,B = MI()

def xor(n):
    if n%2:
        return (n+1)//2%2
    else:
        return ((n+2)//2%2) ^ (n+1)

# Direct XOR of all numbers from 1 to n
def computeXOR(n):
    if (n % 4 == 0):
        return n
    if (n % 4== 1):
        return 1
    if (n % 4 == 2):
        return n + 1
    else:
        return 0

fa = computeXOR(A-1)
fb = computeXOR(B)
print(fa^fb)