"""
https://atcoder.jp/contests/abc324/tasks/abc324_b
B - 3-smooth Numbers

問題文 
正の整数 N が与えられます。 N=2 x 3 y を満たす整数 x,y が存在するなら Yes 、そうでなければ No と出力してください。
"""

N = int(input())

while True:
    if N %2 == 0:
        N = N//2
    else:
        break


while True:
    if N %3 == 0:
        N = N//3
    else:
        break
if N == 1:
    print("Yes")
else:
    print("No")

"""
N <= 10**18以下なので、
"""