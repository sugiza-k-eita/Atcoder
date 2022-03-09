import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = II()
if N  < 3:
    print(0)
    exit()

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
box = koukan(N)
box.sort()
box = box[1:]
ans = []
for i in box:
    i -= 1
    if N//i == N%i:
        ans.append(i)
print(sum(ans))

