#https://atcoder.jp/contests/abc121/submissions/33501062s

def xor(n):
    if n%2:
        return (n+1)//2%2
    else:
        return ((n+2)//2%2) ^ (n+1)

# Direct XOR of all numbers from 1 to n
def computeXOR(n):
    if (n % 4 == 0):
        return n
    if (n % 4 == 1):
        return 1
    if (n % 4 == 2):
        return n + 1
    else:
        return 0