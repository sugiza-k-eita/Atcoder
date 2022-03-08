import sys
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def II(): return int(sys.stdin.readline())
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def S(): return sys.stdin.readline().rstrip()
readline = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

"""
条件
1,Aのほうが小さいこと
2,操作回数に対して、A[i],B[i]の差が収まること

方針
操作回数を求める
前から見ていき、操作回数内にそれぞれの差を0にできるかを考える

Aのほうが大きい場合
差が、Bの操作回数

Bの方が大きい場合
・差が偶数のとき
  //2がAの操作回数
・差が奇数のとき
  //2 + 1がAの操作回数,
  Bは+1操作回数


"""
N = II()
A = LI()
B = LI()

A_sum = sum(A)
B_sum = sum(B)
if B_sum-A_sum < 0:
    print("No")
    exit()

cnt = 0

#A[i]を加算するloop
for i in range(N):
    if A[i] < B[i]:
        x = B[i] - A[i]
        if x % 2 == 0:
            cnt += x//2
            A[i] = B[i]
        else:
            cnt += x//2 + 1
            A[i] = B[i]+1

# print(A,B,cnt)

for i in range(N):
    if A[i] > B[i]:
        cnt -= A[i] -B[i]
        B[i] = A[i]

# print(A,B,cnt)

if cnt >= 0:#Bのほうが大きい分には調整できる
  print("Yes")
else:
  print("No")
