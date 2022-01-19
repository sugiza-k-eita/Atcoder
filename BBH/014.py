import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

#計算量は√n
#入力値が10**9以上ならロー法を使用する
n = II()

def koukan(n):
    ret = []
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n%i ==0:
            ret.append((i,n//i))
            flg = n//i
        if flg <= i:
            break
    return ret

ret = koukan(n)
print(len(str(ret[-1][1])))

