import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()

N = II()
#偶数のときは、その数までに何回10の倍数が出るか？
if N% 2!= 0:
    #奇数の時
    print(0)
    exit()

ans = 0
x = N
five = 10
while five <= 10**19:
    ans += x//five
    five *= 5
print(ans)
        