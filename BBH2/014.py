import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()

#N = A*Bとなるような　A*Bの列挙
def koukan(n):
    ret = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n%i ==0:
            ret.append((i,n//i))
            flg = n//i
        if flg <= i:
            break
    return ret

a = koukan(N)
b,c = a[-1][0],a[-1][1]
print(max(len(str(b)),len(str(c))))
