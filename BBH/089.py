import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)


N = II()
A = LI()


x = 0
y = 0
z = 0
#赤、青、緑の帽子の数を管理。　どの帽子かは、関係ないのであえて命名はx,y,z
ans = 1
for i in range(N):
    if x == A[i] and y == A[i] and z == A[i]:
        #すべて同じ数字なら、i番目は3つの分岐を作る
        ans *= 3
        x += 1
    
    elif x == A[i] and y == A[i]:
        #2つが同じ数字なら、i番目は2つの分岐を作る
        ans *= 2
        x += 1
    
    
    elif x == A[i] and z == A[i]:
        #2つが同じ数字なら、i番目は2つの分岐を作る
        ans *= 2
        x += 1
    
    elif y == A[i] and z == A[i]:
        #2つが同じ数字なら、i番目は2つの分岐を作る
        ans *= 2
        y += 1
    
    elif x == A[i]:
        #条件をみたすのが1つしかないのなら分岐はしない
        x += 1
    elif y == A[i]:
        #条件をみたすのが1つしかないのなら分岐はしない
        y += 1
    elif z == A[i]:
        #条件をみたすのが1つしかないのなら分岐はしない
        z += 1
    
    else:
        #条件をみたすのがないのなら
        print(0)
        exit()
    ans %= 10**9 + 7

print(ans)