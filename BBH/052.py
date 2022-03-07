import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

#N = A*Bとなるような　A*Bの列挙
def koukan(n):
    ret = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n%i ==0:
            ret.append(i)
            ret.append(n//i)
            flg = n//i
        if flg <= i:
            break
    return ret

N,M = MI()
yakusuu = koukan(M)
yakusuu.sort()
yakusuu.reverse()

for i in yakusuu:
    if N <= M/i:
        print(i)
        exit()