import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N,K,X = MI()
A = LI()
sumA = sum(A)
#xより大きい数字は引く　boxに入れる
#クーポン枚数分引く
box = []
cnt = 0
for a in A:
    if a >= X :
        amari = a % X
        box.append(amari)
        cnt += a // X
    else:
        box.append(a)

box.sort(reverse=True)
if cnt >= K:
    ans = sumA - K*X
    print(ans)
else:
    cupon = K - cnt
    minus = cnt*X + sum(box[:cupon])
    ans = sumA - minus
    print(ans)